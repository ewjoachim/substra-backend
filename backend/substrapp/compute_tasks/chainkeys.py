from base64 import b64decode
from os import path
import kubernetes
import os
import logging
import json
from django.conf import settings

logger = logging.getLogger(__name__)

# Chainkeys are used as part of secure aggreagation (separate component, absent from
# this repo)


def prepare_chainkeys_dir(chainkeys_dir: str, k8s_client, compute_plan_tag: str) -> None:
    if os.path.exists(chainkeys_dir):
        # Chainkeys have already been populated
        return

    os.makedirs(chainkeys_dir)
    _prepare_chainkeys(k8s_client, compute_plan_tag, chainkeys_dir)


def _prepare_chainkeys(k8s_client, compute_plan_tag: str, chainkeys_dir: str) -> None:
    secret_namespace = os.getenv("K8S_SECRET_NAMESPACE", "default")
    label_selector = f"compute_plan={compute_plan_tag}"

    # fetch secrets and write them to disk
    try:
        secrets = k8s_client.list_namespaced_secret(secret_namespace, label_selector=label_selector)
    except kubernetes.client.rest.ApiException as e:
        logger.error(f"failed to fetch namespaced secrets {secret_namespace} with selector {label_selector}")
        raise e

    secrets = secrets.to_dict()["items"]
    if not secrets:
        raise Exception(f"No secret found using label selector {label_selector}")

    formatted_secrets = {s["metadata"]["labels"]["index"]: list(b64decode(s["data"]["key"])) for s in secrets}

    with open(path.join(chainkeys_dir, "chainkeys.json"), "w") as f:
        json.dump({"chain_keys": formatted_secrets}, f)
        f.write("\n")  # Add newline cause Py JSON does not

    # remove secrets:
    # do not delete secrets as a running k8s operator will recreate them, instead
    # replace each secret data with an empty dict
    for secret in secrets:
        try:
            k8s_client.replace_namespaced_secret(
                secret["metadata"]["name"],
                secret_namespace,
                body=kubernetes.client.V1Secret(
                    data={},
                    metadata=kubernetes.client.V1ObjectMeta(
                        name=secret["metadata"]["name"],
                        labels=secret["metadata"]["labels"],
                    ),
                ),
            )
        except kubernetes.client.rest.ApiException as e:
            logger.error(f"failed to remove secrets from namespace {secret_namespace}")
            raise e
    else:
        logger.info(f"{len(secrets)} secrets have been removed")

    logger.info(f"Prepared chainkeys: {_list_files(chainkeys_dir)}")


def _list_files(startpath, as_json=True):
    if not settings.TASK["LIST_WORKSPACE"]:
        return "Error: listing files is disabled."

    if not os.path.exists(startpath):
        return f"Error: {startpath} does not exist."

    if as_json:
        return json.dumps(_path_to_dict(startpath))

    res = ""
    for root, dirs, files in os.walk(startpath, followlinks=True):
        level = root.replace(startpath, "").count(os.sep)
        indent = " " * 4 * (level)
        res += f"{indent}{os.path.basename(root)}/" + "\n"
        subindent = " " * 4 * (level + 1)
        for f in files:
            res += f"{subindent}{f}" + "\n"

    return res


def _path_to_dict(path):
    d = {"name": os.path.basename(path)}
    if os.path.isdir(path):
        d["type"] = "directory"
        d["children"] = [_path_to_dict(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        d["type"] = "file"
    return d
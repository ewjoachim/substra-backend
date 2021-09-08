import kubernetes
import os
import logging
from django.conf import settings
from substrapp.utils import timeit
from substrapp.compute_tasks.compute_pod import Label
from substrapp.kubernetes_utils import get_pod_logs, get_security_context, pod_exists, watch_pod, delete_pod
from substrapp.docker_registry import container_image_exists, USER_IMAGE_REPOSITORY
from substrapp.lock_local import lock_resource
from substrapp.compute_tasks.context import Context
from substrapp.exceptions import BuildError
import substrapp.orchestrator.computetask_pb2 as computetask_pb2

logger = logging.getLogger(__name__)

REGISTRY = settings.REGISTRY
REGISTRY_SCHEME = settings.REGISTRY_SCHEME
NAMESPACE = settings.NAMESPACE
KANIKO_MIRROR = settings.TASK["KANIKO_MIRROR"]
KANIKO_IMAGE = settings.TASK["KANIKO_IMAGE"]
KANIKO_DOCKER_CONFIG_SECRET_NAME = settings.TASK["KANIKO_DOCKER_CONFIG_SECRET_NAME"]
COMPUTE_REGISTRY = settings.TASK["COMPUTE_REGISTRY"]
CELERY_WORKER_CONCURRENCY = int(getattr(settings, "CELERY_WORKER_CONCURRENCY"))


def build_images(ctx: Context) -> None:
    build_container_image(ctx.algo_docker_context_dir, ctx.algo_image_tag, ctx)
    if ctx.task_category == computetask_pb2.TASK_TEST:
        build_container_image(ctx.metrics_docker_context_dir, ctx.metrics_image_tag, ctx)


@timeit
def build_container_image(path, tag, ctx):

    if container_image_exists(tag):
        logger.info(f"Image found: {tag}. Using it.")
        return

    _build_container_image(path, tag, ctx.compute_plan_key, ctx.task_key, ctx.attempt)


def _build_container_image(path, tag, cp_key, task_key, attempt):

    _assert_dockerfile(path)

    kubernetes.config.load_incluster_config()
    k8s_client = kubernetes.client.CoreV1Api()

    pod_name = f'kaniko-{tag.split("/")[-1].replace("_", "-")}'

    dockerfile_fullpath = os.path.join(path, "Dockerfile")

    dockerfile_mount_subpath = path.split("/subtuple/")[-1]

    image = KANIKO_IMAGE
    command = None
    mount_path_dockerfile = path

    args = [
        f"--dockerfile={dockerfile_fullpath}",
        f"--context=dir://{path}",
        f"--destination={REGISTRY}/{USER_IMAGE_REPOSITORY}:{tag}",
        "--cache=true",
        "--log-timestamp=true",
        "--snapshotMode=redo",
        "--push-retry=3",
        "--cache-copy-layers",
        "--single-snapshot",
        f"--verbosity={('debug' if settings.LOG_LEVEL == 'DEBUG' else 'info')}",
    ]

    if REGISTRY_SCHEME == "http":
        args.append("--insecure")

    if KANIKO_MIRROR:
        args.append(f"--registry-mirror={REGISTRY}")
        if REGISTRY_SCHEME == "http":
            args.append("--insecure-pull")

    # kaniko build can be launched without privilege but
    # it needs some capabilities and to be root
    # https://github.com/GoogleContainerTools/kaniko/issues/778
    capabilities = ["CHOWN", "SETUID", "SETGID", "FOWNER", "DAC_OVERRIDE"]
    container_security_context = get_security_context(root=True, add_capabilities=capabilities)

    container = kubernetes.client.V1Container(
        name=pod_name,
        image=image if not COMPUTE_REGISTRY else f"{COMPUTE_REGISTRY}/{image}",
        command=command,
        args=args,
        volume_mounts=[
            {
                "name": "dockerfile",
                "mountPath": mount_path_dockerfile,
                "subPath": dockerfile_mount_subpath,
                "readOnly": True,
            }
        ],
        security_context=container_security_context,
    )

    container.volume_mounts.append(
        {
            "name": "cache",
            "mountPath": "/cache",
            "readOnly": True,
        }
    )

    if KANIKO_DOCKER_CONFIG_SECRET_NAME:
        container.volume_mounts.append({"name": "docker-config", "mountPath": "/kaniko/.docker"})

    pod_affinity = kubernetes.client.V1Affinity(
        pod_affinity=kubernetes.client.V1PodAffinity(
            required_during_scheduling_ignored_during_execution=[
                kubernetes.client.V1PodAffinityTerm(
                    label_selector=kubernetes.client.V1LabelSelector(
                        match_expressions=[
                            kubernetes.client.V1LabelSelectorRequirement(
                                key="app.kubernetes.io/component",
                                operator="In",
                                values=["substra-worker"],
                            )
                        ]
                    ),
                    topology_key="kubernetes.io/hostname",
                )
            ]
        )
    )

    spec = kubernetes.client.V1PodSpec(
        restart_policy="Never",
        affinity=pod_affinity,
        containers=[container],
        volumes=[
            {
                "name": "dockerfile",
                "persistentVolumeClaim": {"claimName": settings.K8S_PVC["SUBTUPLE_PVC"]},
            }
        ],
    )

    spec.volumes.append(
        {
            "name": "cache",
            "persistentVolumeClaim": {"claimName": settings.K8S_PVC["DOCKER_CACHE_PVC"]},
        }
    )

    if KANIKO_DOCKER_CONFIG_SECRET_NAME:
        spec.volumes.append(
            {
                "name": "docker-config",
                "secret": {
                    "secretName": KANIKO_DOCKER_CONFIG_SECRET_NAME,
                    "items": [{"key": ".dockerconfigjson", "path": "config.json"}],
                },
            }
        )

    pod = kubernetes.client.V1Pod(
        api_version="v1",
        kind="Pod",
        metadata=kubernetes.client.V1ObjectMeta(
            name=pod_name,
            labels={
                Label.PodName: pod_name,
                Label.PodType: "image-build",
                Label.Component: Label.Component_Compute,
            },
        ),
        spec=spec,
    )

    with lock_resource("image-build", pod_name, ttl=30, timeout=30):
        create_pod = not pod_exists(k8s_client, pod_name)
        if create_pod:
            try:
                logger.info(f"Building image {tag}. Creating pod {NAMESPACE}/{pod_name}")
                k8s_client.create_namespaced_pod(body=pod, namespace=NAMESPACE)
            except kubernetes.client.rest.ApiException as e:
                raise Exception(
                    f"Error creating pod {NAMESPACE}/{pod_name}. Reason: {e.reason}, status: {e.status}, body: {e.body}"
                ) from None

    try:
        watch_pod(k8s_client, pod_name)
    except Exception as e:
        # In case of concurrent build, it may fail
        # check if image exists
        if not container_image_exists(tag):
            logger.error(f"Kaniko build failed, error: {e}")
            raise BuildError(f"Kaniko build failed, error: {e}")
    finally:
        if create_pod:
            log_prefix = f"[{cp_key[:8]}-{task_key[:8]}-b-{attempt}]"
            _container_format_log(pod_name, get_pod_logs(k8s_client, name=pod_name, container=pod_name), log_prefix)
            delete_pod(k8s_client, pod_name)


def _assert_dockerfile(dockerfile_path):
    dockerfile_fullpath = os.path.join(dockerfile_path, "Dockerfile")
    if not os.path.exists(dockerfile_fullpath):
        raise Exception(f"Dockerfile does not exist : {dockerfile_fullpath}")


def _container_format_log(container_name, container_logs, log_prefix):
    if isinstance(container_logs, bytes):
        logs = [f"{log_prefix} {log}" for log in container_logs.decode().split("\n")]
    else:
        logs = [f"{log_prefix} {log}" for log in container_logs.split("\n")]

    for log in logs:
        logger.info(log)

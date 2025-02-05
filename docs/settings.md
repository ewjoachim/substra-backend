
<!-- This file is an auto-generated file, please do not edit manually. Instead you can run `make docs` to update it -->
# Substra setting
This file document all the settings of the substra application

These settings are configured through env variables.
They can be set in the [chart](../charts/substra-backend/README) through the `config` value.

Accepted true values for `bool` are: `1`, `ON`, `On`, `on`, `T`, `t`, `TRUE`, `True`, `true`, `Y`, `y`, `YES`, `yes`; anything else is falsy.

## Global settings

| Type | Setting | Default value | Comment |
|------|---------|---------------|---------|
| json | `ALLOWED_HOSTS` | `[]` |  |
| string | `BACKEND_VERSION` | `dev` |  |
| string | `CELERYBEAT_FLUSH_EXPIRED_TOKENS_TASK_PERIOD` | `86400` (`24 * 3600`) |  |
| string | `CELERYBEAT_MAXIMUM_IMAGES_TTL` | `604800` (`7 * 24 * 3600`) |  |
| string | `CELERY_BROKER_HOST` | `localhost` |  |
| string | `CELERY_BROKER_PASSWORD` | nil |  |
| string | `CELERY_BROKER_PORT` | `5672` |  |
| string | `CELERY_BROKER_USER` | nil |  |
| int | `CELERY_TASK_MAX_RETRIES` | `7` |  |
| int | `CELERY_TASK_RETRY_BACKOFF` | `60` | time in seconds |
| int | `CELERY_TASK_RETRY_BACKOFF_MAX` | `3840` (`64 * 60`) |  |
| int | `CELERY_WORKER_CONCURRENCY` | `1` |  |
| string | `COMMON_HOST_DOMAIN` | nil |  |
| string | `COMPUTE_POD_FS_GROUP` | nil |  |
| int | `COMPUTE_POD_GKE_GPUS_LIMITS` | `0` |  |
| string | `COMPUTE_POD_RUN_AS_GROUP` | nil |  |
| string | `COMPUTE_POD_RUN_AS_USER` | nil |  |
| int | `COMPUTE_POD_STARTUP_TIMEOUT_SECONDS` | `300` |  |
| json | `CSRF_TRUSTED_ORIGINS` | `[]` | A list of origins that are allowed to use unsafe HTTP methods |
| int | `DATA_UPLOAD_MAX_SIZE` | `1073741824` (`1024 * 1024 * 1024`) | bytes |
| bool | `DEBUG_KEEP_POD_AND_DIRS` | `False` |  |
| bool | `DJANGO_LOG_SQL_QUERIES` | `True` |  |
| bool | `ENABLE_DATASAMPLE_STORAGE_IN_SERVERMEDIAS` | `False` |  |
| bool | `ENABLE_METRICS` | `False` |  |
| int | `EXPIRY_TOKEN_LIFETIME` | `1440` (`24 * 60`) | minutes |
| bool | `GZIP_MODELS` | `False` |  |
| string | `HOSTNAME` | nil |  |
| string | `HOST_IP` | nil |  |
| int | `HTTP_CLIENT_TIMEOUT_SECONDS` | `30` |  |
| bool | `ISOLATED` | nil |  |
| string | `K8S_SECRET_NAMESPACE` | `default` |  |
| string | `KANIKO_DOCKER_CONFIG_SECRET_NAME` | nil |  |
| string | `KANIKO_IMAGE` | nil |  |
| bool | `KANIKO_MIRROR` | `False` |  |
| bool | `LOGGING_USE_COLORS` | `True` |  |
| string | `LOG_LEVEL` | `INFO` |  |
| string | `NAMESPACE` | nil |  |
| string | `OBJECTSTORE_ACCESSKEY` | nil |  |
| string | `OBJECTSTORE_SECRETKEY` | nil |  |
| string | `OBJECTSTORE_URL` | nil |  |
| int | `PAGINATION_MAX_PAGE_SIZE` | `10000` |  |
| string | `POD_IP` | nil |  |
| string | `REGISTRY` | nil |  |
| bool | `REGISTRY_IS_LOCAL` | nil |  |
| string | `REGISTRY_PULL_DOMAIN` | nil |  |
| string | `REGISTRY_SCHEME` | nil |  |
| string | `REGISTRY_SERVICE_NAME` | nil |  |
| string | `SUBPATH` | nil |  |
| bool | `TASK_CACHE_DOCKER_IMAGES` | `False` |  |
| bool | `TASK_CHAINKEYS_ENABLED` | `False` |  |
| bool | `TASK_LIST_WORKSPACE` | `True` |  |
| string | `TOKEN_STRATEGY` | `unique` |  |
| string | `WORKER_PVC_DOCKER_CACHE` | nil |  |
| bool | `WORKER_PVC_IS_HOSTPATH` | nil |  |
| string | `WORKER_PVC_SUBTUPLE` | nil |  |
| string | `WORKER_REPLICA_SET_NAME` | nil |  |

## Orchestrator settings

| Type | Setting | Default value | Comment |
|------|---------|---------------|---------|
| int | `ORCHESTRATOR_GRPC_KEEPALIVE_MAX_PINGS_WITHOUT_DATA` | `0` |  |
| int | `ORCHESTRATOR_GRPC_KEEPALIVE_PERMIT_WITHOUT_CALLS` | `0` |  |
| int | `ORCHESTRATOR_GRPC_KEEPALIVE_TIMEOUT_MS` | `20000` |  |
| int | `ORCHESTRATOR_GRPC_KEEPALIVE_TIME_MS` | `60000` |  |
| string | `ORCHESTRATOR_HOST` | nil |  |
| bool | `ORCHESTRATOR_MTLS_ENABLED` | nil |  |
| string | `ORCHESTRATOR_PORT` | nil |  |
| string | `ORCHESTRATOR_TLS_CLIENT_CERT_PATH` | nil |  |
| string | `ORCHESTRATOR_TLS_CLIENT_KEY_PATH` | nil |  |
| bool | `ORCHESTRATOR_TLS_ENABLED` | nil |  |
| string | `ORCHESTRATOR_TLS_SERVER_CACERT_PATH` | nil |  |

## Org settings

| Type | Setting | Default value | Comment |
|------|---------|---------------|---------|
| string | `BACKEND_DEFAULT_PORT` | `8000` |  |
| string | `ORG_NAME` | nil |  |

## CORS settings

| Type | Setting | Default value | Comment |
|------|---------|---------------|---------|
| bool | `CORS_ALLOW_CREDENTIALS` | `False` | If True cookies can be included in cross site requests. Set this to `True` for frontend auth. |
| json | `CORS_ORIGIN_WHITELIST` | `[]` | A list of origins that are authorized to make cross-site HTTP requests (e.g.the frontend url). |

## Ledger settings

| Type | Setting | Default value | Comment |
|------|---------|---------------|---------|
| json | `LEDGER_CHANNELS` | nil |  |
| string | `LEDGER_MSP_ID` | nil |  |

## Worker event app settings

| Type | Setting | Default value | Comment |
|------|---------|---------------|---------|

## API event app settings

| Type | Setting | Default value | Comment |
|------|---------|---------------|---------|

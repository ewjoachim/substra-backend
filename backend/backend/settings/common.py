"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import json
import os
import pathlib
import sys
from datetime import timedelta

import structlog
from django.core.files.storage import FileSystemStorage

from libs.gen_secret_key import write_secret_key

from .deps.org import *

TRUE_VALUES = {"t", "T", "y", "Y", "yes", "YES", "true", "True", "TRUE", "on", "On", "ON", "1", 1, True}


def to_bool(value):
    return value in TRUE_VALUES


def build_broker_url(user: str, pasword: str, host: str, port: str) -> str:
    """Builds a rabbitmq connection string

    Args:
        user (str): rabbitmq user
        pasword (str): rabbitmq password
        host (str): rabbitmq hostname
        port (str): rabbitmq port

    Returns:
        str: a connection string of the form "amqp://user:password@hostname:port//"
    """
    conn_info = ""
    conn_port = ""
    if user and pasword:
        conn_info = f"{user}:{pasword}@"
    if port:
        conn_port = f":{port}"
    return f"amqp://{conn_info}{host}{conn_port}//"


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

sys.path.append(PROJECT_ROOT)
sys.path.append(os.path.normpath(os.path.join(PROJECT_ROOT, "libs")))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_FILE = os.path.normpath(os.path.join(PROJECT_ROOT, "SECRET"))

# KEY CONFIGURATION
# Try to load the SECRET_KEY from our SECRET_FILE. If that fails, then generate
# a random SECRET_KEY and save it into our SECRET_FILE for future loading. If
# everything fails, then just raise an exception.
try:
    SECRET_KEY = pathlib.Path(SECRET_FILE).read_text().strip()
except IOError:
    try:
        SECRET_KEY = write_secret_key(SECRET_FILE)
    except IOError:
        raise Exception(f"Cannot open file `{SECRET_FILE}` for writing.")
# END KEY CONFIGURATION

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SUBPATH = ""
if os.environ.get("SUBPATH"):
    SUBPATH = os.environ.get("SUBPATH").strip("/") + "/"

ALLOWED_HOSTS = ["127.0.0.1", "::1", "localhost"] + json.loads(os.environ.get("ALLOWED_HOSTS", "[]"))
if os.environ.get("HOST_IP"):
    ALLOWED_HOSTS.append(os.environ.get("HOST_IP"))
if os.environ.get("POD_IP"):
    ALLOWED_HOSTS.append(os.environ.get("POD_IP"))

# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django_celery_results",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt.token_blacklist",
    "substrapp",
    "node",
    "users",
    "localrep",
    "drf_spectacular",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "node.authentication.NodeBackend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.RemoteUserMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "libs.health_check_middleware.HealthCheckMiddleware",
    "django_structlog.middlewares.RequestMiddleware",
    "django_structlog.middlewares.CeleryMiddleware",
]


DJANGO_LOG_SQL_QUERIES = to_bool(os.environ.get("DJANGO_LOG_SQL_QUERIES", "True"))
if DJANGO_LOG_SQL_QUERIES:
    MIDDLEWARE.append("libs.sql_printing_middleware.SQLPrintingMiddleware")

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(PROJECT_ROOT, "db.sqlite3"),
    }
}

DATASAMPLE_STORAGE = FileSystemStorage()
MODEL_STORAGE = FileSystemStorage()
ALGO_STORAGE = FileSystemStorage()
DATAMANAGER_STORAGE = FileSystemStorage()
METRICS_STORAGE = FileSystemStorage()
COMPUTE_TASK_LOGS_STORAGE = FileSystemStorage()

OBJECTSTORE_URL = os.environ.get("OBJECTSTORE_URL")
OBJECTSTORE_ACCESSKEY = os.environ.get("OBJECTSTORE_ACCESSKEY")
OBJECTSTORE_SECRETKEY = os.environ.get("OBJECTSTORE_SECRETKEY")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/tmp/django_cache",  # nosec
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "libs.zxcvbn_validator.ZxcvbnValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 9,
        },
    },
    {"NAME": "libs.maximum_length_validator.MaximumLengthValidator", "OPTIONS": {"max_length": 64}},
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = f"/{SUBPATH}static/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "medias")
SITE_ID = 1

TASK = {
    "CACHE_DOCKER_IMAGES": to_bool(os.environ.get("TASK_CACHE_DOCKER_IMAGES", False)),
    "CHAINKEYS_ENABLED": to_bool(os.environ.get("TASK_CHAINKEYS_ENABLED", False)),
    "LIST_WORKSPACE": to_bool(os.environ.get("TASK_LIST_WORKSPACE", True)),
    "KANIKO_MIRROR": to_bool(os.environ.get("KANIKO_MIRROR", False)),
    "KANIKO_IMAGE": os.environ.get("KANIKO_IMAGE"),
    "KANIKO_DOCKER_CONFIG_SECRET_NAME": os.environ.get("KANIKO_DOCKER_CONFIG_SECRET_NAME"),
    "COMPUTE_POD_STARTUP_TIMEOUT_SECONDS": int(os.environ.get("COMPUTE_POD_STARTUP_TIMEOUT_SECONDS", 300)),
}

CELERY_BROKER_USER = os.environ.get("CELERY_BROKER_USER")
CELERY_BROKER_PASSWORD = os.environ.get("CELERY_BROKER_PASSWORD")
CELERY_BROKER_HOST = os.environ.get("CELERY_BROKER_HOST", "localhost")
CELERY_BROKER_PORT = os.environ.get("CELERY_BROKER_PORT", "5672")
CELERY_BROKER_URL = build_broker_url(CELERY_BROKER_USER, CELERY_BROKER_PASSWORD, CELERY_BROKER_HOST, CELERY_BROKER_PORT)

CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TASK_TRACK_STARTED = True  # since 4.0

# With these settings, tasks will be retried for up to a maximum of 127 minutes.
#
# max_wait = CELERY_TASK_RETRY_BACKOFF * sum(2 ** n for n in range(CELERY_TASK_MAX_RETRIES))
#          = 60 * (1 + 2 + 4 + 8 + 16 + 32 + 64)
#          = 127 minutes
#
# Since jitter is enabled, the actual cumulative wait can be much less than max_wait. From the doc
# (https://docs.celeryproject.org/en/stable/userguide/tasks.html#Task.retry_jitter):
#
# > If this option is set to True, the delay value calculated by retry_backoff is treated as a maximum, and the actual
# > delay value will be a random number between zero and that maximum.
CELERY_TASK_AUTORETRY_FOR = (Exception,)  # Retry on any exception
CELERY_TASK_MAX_RETRIES = int(os.environ.get("CELERY_TASK_MAX_RETRIES", 7))
CELERY_TASK_RETRY_BACKOFF = int(os.environ.get("CELERY_TASK_RETRY_BACKOFF", 60))  # time in seconds
CELERY_TASK_RETRY_BACKOFF_MAX = int(os.environ.get("CELERY_TASK_RETRY_BACKOFF_MAX", 64 * 60))
CELERY_TASK_RETRY_JITTER = True

CELERY_WORKER_CONCURRENCY = int(os.environ.get("CELERY_WORKER_CONCURRENCY", 1))
CELERY_BROADCAST = f"{ORG_NAME}.broadcast"

CELERYBEAT_MAXIMUM_IMAGES_TTL = os.environ.get("CELERYBEAT_MAXIMUM_IMAGES_TTL", 7 * 24 * 3600)
CELERYBEAT_FLUSH_EXPIRED_TOKENS_TASK_PERIOD = os.environ.get("CELERYBEAT_FLUSH_EXPIRED_TOKENS_TASK_PERIOD", 24 * 3600)
CELERYBEAT_SCHEDULE_TASK_PERIOD = os.environ.get("CELERYBEAT_SCHEDULE_TASK_PERIOD", 3 * 3600)

WORKER_PVC_IS_HOSTPATH = to_bool(os.environ.get("WORKER_PVC_IS_HOSTPATH"))
WORKER_PVC_DOCKER_CACHE = os.environ.get("WORKER_PVC_DOCKER_CACHE")
WORKER_PVC_SUBTUPLE = os.environ.get("WORKER_PVC_SUBTUPLE")
WORKER_REPLICA_SET_NAME = os.environ.get("WORKER_REPLICA_SET_NAME")


NAMESPACE = os.getenv("NAMESPACE")

REGISTRY = os.getenv("REGISTRY")
REGISTRY_SCHEME = os.getenv("REGISTRY_SCHEME")
REGISTRY_PULL_DOMAIN = os.getenv("REGISTRY_PULL_DOMAIN")
REGISTRY_IS_LOCAL = to_bool(os.environ.get("REGISTRY_IS_LOCAL"))
REGISTRY_SERVICE_NAME = os.environ.get("REGISTRY_SERVICE_NAME")

COMPUTE_POD_RUN_AS_USER = os.environ.get("COMPUTE_POD_RUN_AS_USER")
COMPUTE_POD_RUN_AS_GROUP = os.environ.get("COMPUTE_POD_RUN_AS_GROUP")
COMPUTE_POD_FS_GROUP = os.environ.get("COMPUTE_POD_FS_GROUP")
COMPUTE_POD_GKE_GPUS_LIMITS = int(os.environ.get("COMPUTE_POD_GKE_GPUS_LIMITS", 0))

# Prometheus configuration
ENABLE_METRICS = to_bool(os.environ.get("ENABLE_METRICS", False))
# Keeping migrations enabled leads to issues with collectsatic
PROMETHEUS_EXPORT_MIGRATIONS = False
if ENABLE_METRICS:
    # Enable tasks related events so that tasks can be monitored
    CELERY_WORKER_SEND_TASK_EVENTS = True
    CELERY_TASK_SEND_SENT_EVENT = True

    INSTALLED_APPS.append("django_prometheus")
    MIDDLEWARE = (
        ["django_prometheus.middleware.PrometheusBeforeMiddleware"]
        + MIDDLEWARE
        + ["django_prometheus.middleware.PrometheusAfterMiddleware"]
    )


DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

# Uploaded file max size, in bytes
DATA_UPLOAD_MAX_SIZE = int(os.environ.get("DATA_UPLOAD_MAX_SIZE", 1024 * 1024 * 1024))

EXPIRY_TOKEN_LIFETIME = timedelta(minutes=int(os.environ.get("EXPIRY_TOKEN_LIFETIME", 24 * 60)))
TOKEN_STRATEGY = os.environ.get("TOKEN_STRATEGY", "unique")

GZIP_MODELS = to_bool(os.environ.get("GZIP_MODELS", False))

HTTP_CLIENT_TIMEOUT_SECONDS = int(os.environ.get("HTTP_CLIENT_TIMEOUT_SECONDS", 30))

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOGGING_USE_COLORS = to_bool(os.environ.get("LOGGING_USE_COLORS", True))

# With DEBUG_QUICK_IMAGE, container images are never deleted, and image names are based on the algo/metrics checksum
# (instead of algo/metrics key, without the option). This allows reuse of images and significantly speeds up end-to-end
# tests.
DEBUG_QUICK_IMAGE = to_bool(os.environ.get("DEBUG_QUICK_IMAGE", False))
DEBUG_KEEP_POD_AND_DIRS = to_bool(os.environ.get("DEBUG_KEEP_POD_AND_DIRS", False))

PAGINATION_MAX_PAGE_SIZE = int(os.environ.get("PAGINATION_MAX_PAGE_SIZE", 100))

pre_chain = [
    structlog.processors.TimeStamper(fmt="iso"),
    structlog.stdlib.add_logger_name,
    structlog.stdlib.add_log_level,
]
ENABLE_DATASAMPLE_STORAGE_IN_SERVERMEDIAS = to_bool(os.environ.get("ENABLE_DATASAMPLE_STORAGE_IN_SERVERMEDIAS", False))

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "key_value": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.JSONRenderer(),
            "foreign_pre_chain": pre_chain,
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "key_value",
        },
    },
    "loggers": {
        # root logger
        "": {
            "level": "WARNING",
            "handlers": ["console"],
            "propagate": True,
        },
        # django and its applications
        "django": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "substrapp": {
            "level": LOG_LEVEL,
            "handlers": ["console"],
            "propagate": False,
        },
        "events": {
            "level": LOG_LEVEL,
            "handlers": ["console"],
            "propagate": False,
        },
        # third-party libraries
        "celery": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": True,
        },
    },
}

BACKEND_VERSION = os.environ.get("BACKEND_VERSION")

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

COMMON_HOST_DOMAIN = os.environ.get("COMMON_HOST_DOMAIN")

ISOLATED = to_bool(os.environ.get("ISOLATED"))

CONTENT_DISPOSITION_HEADER = {}

LOCALREP_RESYNC_EVENTS_PAGE_SIZE = int(os.environ.get("LOCALREP_RESYNC_EVENTS_PAGE_SIZE", 1000))

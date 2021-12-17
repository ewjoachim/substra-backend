import logging
import tempfile

from .common import *
from .deps.cors import *
from .deps.restframework import *

logging.disable(logging.CRITICAL)

ORG_NAME = "OrgTestSuite"
DEFAULT_DOMAIN = "http://testserver"

ASSET_BUFFER_DIR = tempfile.mkdtemp()  # overridden in individual tests
SUBTUPLE_DIR = os.path.join(MEDIA_ROOT, "subtuple")
SUBTUPLE_TMP_DIR = os.path.join(SUBTUPLE_DIR, "tmp")

ORCHESTRATOR_HOST = "orchestrator"
ORCHESTRATOR_PORT = 9000
ORCHESTRATOR_TLS_ENABLED = False
ORCHESTRATOR_MTLS_ENABLED = False

ORCHESTRATOR_RABBITMQ_HOST = "rabbit"
ORCHESTRATOR_RABBITMQ_PORT = 5672
ORCHESTRATOR_RABBITMQ_AUTH_USER = "user"
ORCHESTRATOR_RABBITMQ_AUTH_PASSWORD = "password"
ORCHESTRATOR_RABBITMQ_TLS_ENABLED = False

LEDGER_MSP_ID = "testOrgMSP"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("BACKEND_DB_NAME", "substra"),
        "USER": os.environ.get("BACKEND_DB_USER", "postgres"),
        "PASSWORD": os.environ.get("BACKEND_DB_PWD", "postgres"),
        "HOST": os.environ.get("BACKEND_DB_HOST", "localhost"),
        "PORT": os.environ.get("BACKEND_DB_PORT", 5432),
    }
}

import tempfile

import structlog
from django.conf import settings
from django.urls.base import reverse
from django.views.decorators import gzip
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from libs.pagination import DefaultPageNumberPagination
from libs.pagination import PaginationMixin
from node.authentication import NodeUser
from substrapp.clients import node as node_client
from substrapp.models import Model
from substrapp.orchestrator import get_orchestrator_client
from substrapp.views.filters_utils import filter_list
from substrapp.views.utils import AssetPermissionError
from substrapp.views.utils import PermissionMixin
from substrapp.views.utils import get_channel_name
from substrapp.views.utils import if_true
from substrapp.views.utils import validate_key

logger = structlog.get_logger(__name__)


def replace_storage_addresses(request, model):
    # Here we might need to check if there is a storage address, might not be the case with
    # delete_intermediary_model
    if "address" in model and model["address"]:
        model["address"]["storage_address"] = request.build_absolute_uri(
            reverse("substrapp:model-file", args=[model["key"]])
        )


class ModelViewSet(PaginationMixin, GenericViewSet):
    queryset = Model.objects.all()
    pagination_class = DefaultPageNumberPagination

    def create_or_update_model(self, channel_name, traintuple, key):
        if traintuple["out_model"] is None:
            raise Exception(f"This traintuple related to this model key {key} does not have a out_model")

        # get model from remote node
        url = traintuple["out_model"]["storage_address"]

        content = node_client.get(channel_name, traintuple["creator"], url, traintuple["key"])

        # write model in local db for later use
        tmp_model = tempfile.TemporaryFile()
        tmp_model.write(content)
        instance, created = Model.objects.update_or_create(key=key)
        instance.file.save("model", tmp_model)

        return instance

    def _retrieve(self, request, key):
        validated_key = validate_key(key)

        with get_orchestrator_client(get_channel_name(request)) as client:
            data = client.query_model(validated_key)

        replace_storage_addresses(request, data)

        return data

    def retrieve(self, request, *args, **kwargs):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        key = self.kwargs[lookup_url_kwarg]

        data = self._retrieve(request, key)
        return Response(data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        with get_orchestrator_client(get_channel_name(request)) as client:
            data = client.query_models()

        query_params = request.query_params.get("search")
        if query_params is not None:
            data = filter_list(
                object_type="model",
                data=data,
                query_params=query_params,
            )

        for model in data:
            replace_storage_addresses(request, model)

        return self.paginate_response(data)


class ModelPermissionViewSet(PermissionMixin, GenericViewSet):

    queryset = Model.objects.all()

    def check_access(self, channel_name: str, user, asset, is_proxied_request: bool) -> None:
        """Return true if API consumer is allowed to access the model.

        Args:
            is_proxied_request: True if the API consumer is another backend-server proxying a user request

        Raises:
            AssetPermissionError
        """
        if user.is_anonymous:
            raise AssetPermissionError()

        elif type(user) is NodeUser and is_proxied_request:  # Export request (proxied)
            self._check_export_enabled(channel_name)
            self._check_permission("download", asset, node_id=user.username)

        elif type(user) is NodeUser:  # Node-to-node download
            self._check_permission("process", asset, node_id=user.username)

        else:  # user is an end-user (not a NodeUser): this is an export request
            self._check_export_enabled(channel_name)
            self._check_permission("download", asset, node_id=settings.LEDGER_MSP_ID)

    @staticmethod
    def _check_export_enabled(channel_name):
        channel = settings.LEDGER_CHANNELS[channel_name]
        if not channel.get("model_export_enabled", False):
            raise AssetPermissionError(f"Disabled: model_export_enabled is disabled on {settings.LEDGER_MSP_ID}")

    @staticmethod
    def _check_permission(permission_type, asset, node_id):
        permissions = asset["permissions"][permission_type]
        if not permissions["public"] and node_id not in permissions["authorized_ids"]:
            raise AssetPermissionError(f'{node_id} doesn\'t have permission to download model {asset["key"]}')

    @if_true(gzip.gzip_page, settings.GZIP_MODELS)
    @action(detail=True)
    def file(self, request, *args, **kwargs):
        return self.download_file(
            request, query_method="query_model", django_field="file", orchestrator_field="address"
        )

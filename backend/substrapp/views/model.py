import structlog
from django.conf import settings
from django.urls.base import reverse
from django.views.decorators import gzip
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import GenericViewSet

import orchestrator.model_pb2 as model_pb2
from libs.pagination import DefaultPageNumberPagination
from localrep.models import Model as ModelRep
from localrep.serializers import ModelSerializer as ModelRepSerializer
from node.authentication import NodeUser
from substrapp.models import Model
from substrapp.utils import get_owner
from substrapp.views.filters_utils import filter_queryset
from substrapp.views.utils import ApiResponse
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


class ModelViewSet(GenericViewSet):
    queryset = Model.objects.all()
    pagination_class = DefaultPageNumberPagination

    def _retrieve(self, request, key):
        validated_key = validate_key(key)

        try:
            model = ModelRep.objects.filter(channel=get_channel_name(request)).get(key=validated_key)
        except ModelRep.DoesNotExist:
            raise NotFound
        data = ModelRepSerializer(model).data

        replace_storage_addresses(request, data)

        return data

    def retrieve(self, request, *args, **kwargs):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        key = self.kwargs[lookup_url_kwarg]

        data = self._retrieve(request, key)
        return ApiResponse(data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = ModelRep.objects.filter(channel=get_channel_name(request)).order_by("creation_date", "key")

        query_params = request.query_params.get("search")
        if query_params is not None:

            def map_category(key, values):
                if key == "category":
                    values = [model_pb2.ModelCategory.Value(value) for value in values]
                return key, values

            queryset = filter_queryset("model", queryset, query_params, mapping_callback=map_category)
        queryset = self.paginate_queryset(queryset)

        data = ModelRepSerializer(queryset, many=True).data
        for model in data:
            replace_storage_addresses(request, model)

        return self.get_paginated_response(data)


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
            field, node_id = "download", user.username

        elif type(user) is NodeUser:  # Node-to-node download
            field, node_id = "process", user.username

        else:  # user is an end-user (not a NodeUser): this is an export request
            self._check_export_enabled(channel_name)
            field, node_id = "download", get_owner()

        if not asset.is_public(field) and node_id not in asset.get_authorized_ids(field):
            raise AssetPermissionError()

    @staticmethod
    def _check_export_enabled(channel_name):
        channel = settings.LEDGER_CHANNELS[channel_name]
        if not channel.get("model_export_enabled", False):
            raise AssetPermissionError(f"Disabled: model_export_enabled is disabled on {settings.LEDGER_MSP_ID}")

    @if_true(gzip.gzip_page, settings.GZIP_MODELS)
    @action(detail=True)
    def file(self, request, *args, **kwargs):
        return self.download_file(request, ModelRep, "file", "model_address")

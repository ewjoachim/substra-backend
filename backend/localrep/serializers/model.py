from rest_framework import serializers

import orchestrator.model_pb2 as model_pb2
from localrep.models import ComputeTask
from localrep.models import Model
from localrep.serializers.utils import SafeSerializerMixin
from localrep.serializers.utils import get_channel_choices
from localrep.serializers.utils import make_addressable_serializer
from localrep.serializers.utils import make_download_process_permission_serializer


class CategoryField(serializers.Field):
    def to_representation(self, value):
        return model_pb2.ModelCategory.Name(value)

    def to_internal_value(self, value):
        return model_pb2.ModelCategory.Value(value)


class ModelSerializer(serializers.ModelSerializer, SafeSerializerMixin):
    category = CategoryField()
    compute_task_key = serializers.PrimaryKeyRelatedField(
        queryset=ComputeTask.objects.all(), source="compute_task", pk_field=serializers.UUIDField(format="hex_verbose")
    )
    channel = serializers.ChoiceField(choices=get_channel_choices(), write_only=True)
    address = make_addressable_serializer("model")(source="*")
    permissions = make_download_process_permission_serializer()(source="*")

    class Meta:
        model = Model
        fields = [
            "address",
            "category",
            "channel",
            "compute_task_key",
            "creation_date",
            "key",
            "owner",
            "permissions",
        ]

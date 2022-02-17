import copy

from rest_framework import serializers

import orchestrator.computetask_pb2 as computetask_pb2
from localrep.models import Algo
from localrep.models import ComputePlan
from localrep.models import ComputeTask
from localrep.models import DataManager
from localrep.models import DataSample
from localrep.models import Metric
from localrep.serializers import AlgoSerializer
from localrep.serializers.utils import SafeSerializerMixin
from localrep.serializers.utils import get_channel_choices
from localrep.serializers.utils import make_download_process_permission_serializer
from localrep.serializers.utils import make_permission_serializer


class CategoryField(serializers.Field):
    def to_representation(self, instance):
        return computetask_pb2.ComputeTaskCategory.Name(instance)

    def to_internal_value(self, data):
        return computetask_pb2.ComputeTaskCategory.Value(data)


class StatusField(serializers.Field):
    def to_representation(self, instance):
        return computetask_pb2.ComputeTaskStatus.Name(instance)

    def to_internal_value(self, data):
        return computetask_pb2.ComputeTaskStatus.Value(data)


class AlgoField(serializers.Field):
    def to_representation(self, data):
        return AlgoSerializer(instance=data).data

    def to_internal_value(self, data):
        return Algo.objects.get(key=data["key"])


class ComputeTaskSerializer(serializers.ModelSerializer, SafeSerializerMixin):
    category = CategoryField()
    status = StatusField()
    logs_permission = make_permission_serializer("logs_permission")(source="*")

    algo = AlgoField()

    compute_plan_key = serializers.PrimaryKeyRelatedField(queryset=ComputePlan.objects.all(), source="compute_plan")
    parent_task_keys = serializers.ListField(source="parent_tasks", child=serializers.CharField(), required=False)
    channel = serializers.ChoiceField(choices=get_channel_choices(), write_only=True)

    data_manager_key = serializers.PrimaryKeyRelatedField(
        queryset=DataManager.objects.all(), source="data_manager", required=False
    )
    data_sample_keys = serializers.PrimaryKeyRelatedField(
        queryset=DataSample.objects.all(), many=True, source="data_samples", required=False
    )
    metric_keys = serializers.PrimaryKeyRelatedField(
        queryset=Metric.objects.all(), many=True, source="metrics", required=False
    )
    model_permissions = make_download_process_permission_serializer("model_")(source="*", required=False)
    head_permissions = make_download_process_permission_serializer("head_", public=False)(source="*", required=False)
    trunk_permissions = make_download_process_permission_serializer("trunk_", public=False)(source="*", required=False)

    def to_internal_value(self, data):
        prepared_data = copy.deepcopy(data)
        task_category = computetask_pb2.ComputeTaskCategory.Value(data["category"])
        if task_category == computetask_pb2.TASK_TRAIN:
            prepared_data["data_manager_key"] = data["train"]["data_manager_key"]
            prepared_data["data_sample_keys"] = data["train"]["data_sample_keys"]
            prepared_data["model_permissions"] = data["train"]["model_permissions"]
        elif task_category == computetask_pb2.TASK_TEST:
            prepared_data["data_manager_key"] = data["test"]["data_manager_key"]
            prepared_data["data_sample_keys"] = data["test"]["data_sample_keys"]
            prepared_data["metric_keys"] = data["test"]["metric_keys"]
        elif task_category == computetask_pb2.TASK_AGGREGATE:
            prepared_data["model_permissions"] = data["aggregate"]["model_permissions"]
        elif task_category == computetask_pb2.TASK_COMPOSITE:
            prepared_data["data_manager_key"] = data["composite"]["data_manager_key"]
            prepared_data["data_sample_keys"] = data["composite"]["data_sample_keys"]
            prepared_data["head_permissions"] = data["composite"]["head_permissions"]
            prepared_data["trunk_permissions"] = data["composite"]["trunk_permissions"]
        return super().to_internal_value(prepared_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.category == computetask_pb2.TASK_TRAIN:
            data["train"] = {
                "data_manager_key": data["data_manager_key"],
                "data_sample_keys": data["data_sample_keys"],
                "model_permissions": data["model_permissions"],
            }
        elif instance.category == computetask_pb2.TASK_TEST:
            data["test"] = {
                "data_manager_key": data["data_manager_key"],
                "data_sample_keys": data["data_sample_keys"],
                "metric_keys": data["metric_keys"],
            }
        elif instance.category == computetask_pb2.TASK_AGGREGATE:
            data["aggregate"] = {"model_permissions": data["model_permissions"]}
        elif instance.category == computetask_pb2.TASK_COMPOSITE:
            data["composite"] = {
                "data_manager_key": data["data_manager_key"],
                "data_sample_keys": data["data_sample_keys"],
                "head_permissions": data["head_permissions"],
                "trunk_permissions": data["trunk_permissions"],
            }
        del data["data_manager_key"]
        del data["data_sample_keys"]
        del data["metric_keys"]
        del data["model_permissions"]
        del data["head_permissions"]
        del data["trunk_permissions"]

        return data

    class Meta:
        model = ComputeTask
        fields = [
            "algo",
            "category",
            "channel",
            "compute_plan_key",
            "creation_date",
            "data_manager_key",
            "data_sample_keys",
            "head_permissions",
            "key",
            "logs_permission",
            "metadata",
            "metric_keys",
            "model_permissions",
            "owner",
            "parent_task_keys",
            "rank",
            "status",
            "trunk_permissions",
            "worker",
        ]
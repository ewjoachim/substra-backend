from django.db import transaction
from django.urls import reverse
from rest_framework import serializers

import orchestrator.failure_report_pb2 as failure_report_pb2
from api.models import Algo
from api.models import AlgoInput
from api.models import AlgoOutput
from api.models import ComputePlan
from api.models import ComputeTask
from api.models import ComputeTaskInput
from api.models import ComputeTaskInputAsset
from api.models import ComputeTaskOutput
from api.models import DataManager
from api.models import DataSample
from api.models import Model
from api.models import Performance
from api.models.computetask import TaskDataSamples
from api.serializers.algo import AlgoSerializer
from api.serializers.datamanager import DataManagerSerializer
from api.serializers.model import ModelSerializer
from api.serializers.performance import PerformanceSerializer
from api.serializers.utils import SafeSerializerMixin
from api.serializers.utils import get_channel_choices
from api.serializers.utils import make_download_process_permission_serializer
from api.serializers.utils import make_permission_serializer
from substrapp.compute_tasks.errors import ComputeTaskErrorType

TASK_CATEGORY_FIELDS = {
    ComputeTask.Category.TASK_TRAIN: "train",
    ComputeTask.Category.TASK_PREDICT: "predict",
    ComputeTask.Category.TASK_TEST: "test",
    ComputeTask.Category.TASK_COMPOSITE: "composite",
    ComputeTask.Category.TASK_AGGREGATE: "aggregate",
}


class ComputeTaskInputSerializer(serializers.ModelSerializer, SafeSerializerMixin):
    class Meta:
        model = ComputeTaskInput
        fields = [
            "identifier",
            "asset_key",
            "parent_task_key",
            "parent_task_output_identifier",
            "asset",
        ]

    asset = serializers.SerializerMethodField(source="*", read_only=True)

    def to_representation(self, data):
        data = super().to_representation(data)
        asset_data = data.pop("asset")
        data.update(asset_data)
        return data

    def get_asset(self, task_input):
        data = {}
        try:
            if task_input.asset.asset_kind == AlgoInput.Kind.ASSET_DATA_MANAGER:
                data_manager = DataManager.objects.get(key=task_input.asset.asset_key)
                data_manager_data = DataManagerSerializer(context=self.context, instance=data_manager).data
                data["addressable"] = data_manager_data["opener"]
                data["permissions"] = data_manager_data["permissions"]
            elif task_input.asset.asset_kind == AlgoInput.Kind.ASSET_MODEL:
                model = Model.objects.get(key=task_input.asset.asset_key)
                model_data = ModelSerializer(context=self.context, instance=model).data
                data["addressable"] = model_data["address"]
                data["permissions"] = model_data["permissions"]
        except ComputeTaskInputAsset.DoesNotExist:
            pass
        return data


class ComputeTaskOutputSerializer(serializers.ModelSerializer, SafeSerializerMixin):
    class Meta:
        model = ComputeTaskOutput
        fields = [
            "identifier",
            "permissions",
            "transient",
            "value",
        ]

    permissions = make_download_process_permission_serializer()(source="*")
    value = serializers.SerializerMethodField(source="*", read_only=True)

    def get_value(self, task_output):
        data = []
        for output_asset in task_output.assets.all():
            if output_asset.asset_kind == AlgoOutput.Kind.ASSET_MODEL:
                model = Model.objects.get(key=output_asset.asset_key)
                data.append(ModelSerializer(context=self.context, instance=model).data)
            elif output_asset.asset_kind == AlgoOutput.Kind.ASSET_PERFORMANCE:
                task_key, metric_key = output_asset.asset_key.split("|")
                perf = Performance.objects.get(compute_task__key=task_key, metric__key=metric_key)
                data.append(perf.value)

        # FIXME: we should better always return a list,
        # but it may requires some adapations on the frontend side
        if len(data) == 0:
            return None
        elif len(data) == 1:
            return data[0]
        else:
            return data


class AlgoField(serializers.Field):
    def to_representation(self, data):
        return AlgoSerializer(instance=data).data

    def to_internal_value(self, data):
        return Algo.objects.get(key=data["key"])


class PredictTaskSerializer(serializers.Serializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["models"] = data["models"] or None  # sdk does not support empty list
        return data

    data_manager_key = serializers.PrimaryKeyRelatedField(
        queryset=DataManager.objects.all(),
        source="data_manager",
        required=False,
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )
    data_sample_keys = serializers.PrimaryKeyRelatedField(
        queryset=DataSample.objects.all(),
        source="data_samples",
        many=True,
        required=False,
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )
    models = ModelSerializer(many=True, read_only=True)

    class Meta:
        fields = ["data_manager_key", "data_sample_keys", "models"]


class TestTaskSerializer(serializers.Serializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["perfs"] = {perf["metric_key"]: perf["performance_value"] for perf in data["perfs"]} or None
        return data

    data_manager_key = serializers.PrimaryKeyRelatedField(
        queryset=DataManager.objects.all(),
        source="data_manager",
        required=False,
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )
    data_sample_keys = serializers.PrimaryKeyRelatedField(
        queryset=DataSample.objects.all(),
        source="data_samples",
        many=True,
        required=False,
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )
    perfs = PerformanceSerializer(many=True, read_only=True, source="performances")

    class Meta:
        fields = ["data_manager_key", "data_sample_keys", "perfs"]


class TrainTaskSerializer(serializers.Serializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["models"] = data["models"] or None  # sdk does not support empty list
        return data

    data_manager_key = serializers.PrimaryKeyRelatedField(
        queryset=DataManager.objects.all(),
        source="data_manager",
        required=False,
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )
    data_sample_keys = serializers.PrimaryKeyRelatedField(
        queryset=DataSample.objects.all(),
        source="data_samples",
        many=True,
        required=False,
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )
    models = ModelSerializer(many=True, read_only=True)

    class Meta:
        fields = ["data_manager_key", "data_sample_keys", "models"]


class AggregateTaskSerializer(serializers.Serializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["models"] = data["models"] or None  # sdk does not support empty list
        return data

    models = ModelSerializer(many=True, read_only=True)

    class Meta:
        fields = ["models"]


class CompositeTaskSerializer(serializers.Serializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["models"] = data["models"] or None  # sdk does not support empty list
        return data

    data_manager_key = serializers.PrimaryKeyRelatedField(
        queryset=DataManager.objects.all(),
        source="data_manager",
        required=False,
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )

    data_sample_keys = serializers.PrimaryKeyRelatedField(
        queryset=DataSample.objects.all(),
        source="data_samples",
        many=True,
        required=False,
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )
    models = ModelSerializer(many=True, read_only=True)

    class Meta:
        fields = ["data_manager_key", "data_sample_keys", "models"]


class ComputeTaskSerializer(serializers.ModelSerializer, SafeSerializerMixin):
    logs_permission = make_permission_serializer("logs_permission")(source="*")
    algo = AlgoField()

    # Need to set `pk_field` for `PrimaryKeyRelatedField` in order to correctly serialize `UUID` to `str`
    # See: https://stackoverflow.com/a/51636009
    compute_plan_key = serializers.PrimaryKeyRelatedField(
        queryset=ComputePlan.objects.all(),
        source="compute_plan",
        pk_field=serializers.UUIDField(format="hex_verbose"),
    )
    channel = serializers.ChoiceField(choices=get_channel_choices(), write_only=True)

    duration = serializers.IntegerField(read_only=True)
    inputs = ComputeTaskInputSerializer(many=True)
    outputs = ComputeTaskOutputSerializer(many=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # error_type
        if data["error_type"] is not None:
            data["error_type"] = ComputeTaskErrorType.from_int(
                failure_report_pb2.ErrorType.Value(data["error_type"])
            ).name

        # replace storage addresses
        self._replace_storage_addresses(data)

        data["outputs"] = {_output.pop("identifier"): _output for _output in data["outputs"]}

        return data

    def _replace_storage_addresses(self, task):
        request = self.context.get("request")
        if not request:
            return task

        # replace in common relationships
        if "algo" in task:
            task["algo"]["description"]["storage_address"] = request.build_absolute_uri(
                reverse("api:algo-description", args=[task["algo"]["key"]])
            )
            task["algo"]["algorithm"]["storage_address"] = request.build_absolute_uri(
                reverse("api:algo-file", args=[task["algo"]["key"]])
            )

    class Meta:
        model = ComputeTask
        fields = [
            "algo",
            "channel",
            "compute_plan_key",
            "creation_date",
            "end_date",
            "error_type",
            "key",
            "logs_permission",
            "metadata",
            "owner",
            "rank",
            "start_date",
            "status",
            "tag",
            "worker",
            "duration",
            "inputs",
            "outputs",
        ]


class LegacyComputeTaskSerializer(ComputeTaskSerializer):
    predict = PredictTaskSerializer(required=False, source="*")
    test = TestTaskSerializer(required=False, source="*")
    train = TrainTaskSerializer(required=False, source="*")
    aggregate = AggregateTaskSerializer(required=False, source="*")
    composite = CompositeTaskSerializer(required=False, source="*")
    parent_task_keys = serializers.ListField(source="parent_tasks", child=serializers.CharField(), required=False)

    @transaction.atomic
    def create(self, validated_data):
        data_samples = []
        if "data_samples" in validated_data:
            data_samples = validated_data.pop("data_samples")

        inputs = validated_data.pop("inputs")
        outputs = validated_data.pop("outputs")

        compute_task = super().create(validated_data)
        input_kinds = {algo_input.identifier: algo_input.kind for algo_input in compute_task.algo.inputs.all()}

        for order, data_sample in enumerate(data_samples):
            TaskDataSamples.objects.create(compute_task=compute_task, data_sample=data_sample, order=order)

        for position, input in enumerate(inputs):
            task_input = ComputeTaskInput.objects.create(
                channel=compute_task.channel,
                task=compute_task,
                position=position,
                **input,
            )
            # task input asset could be known during task registration
            # or could be resolved later if it does not exist yet
            if task_input.asset_key:
                ComputeTaskInputAsset.objects.create(
                    channel=compute_task.channel,
                    task_input=task_input,
                    asset_key=task_input.asset_key,
                    asset_kind=input_kinds[task_input.identifier],
                )
            elif task_input.parent_task_key:
                task_output = ComputeTaskOutput.objects.get(
                    task=task_input.parent_task_key,
                    identifier=task_input.parent_task_output_identifier,
                )
                # this only supports a single asset per output for now
                task_output_asset = task_output.assets.first()
                if task_output_asset:
                    ComputeTaskInputAsset.objects.create(
                        channel=compute_task.channel,
                        task_input=task_input,
                        asset_key=task_output_asset.asset_key,
                        asset_kind=input_kinds[task_input.identifier],
                    )

        for output in outputs:
            ComputeTaskOutput.objects.create(
                channel=compute_task.channel,
                task=compute_task,
                **output,
            )

        compute_task.refresh_from_db()
        return compute_task

    def to_representation(self, instance):
        data = super().to_representation(instance)

        for category, field in TASK_CATEGORY_FIELDS.items():
            if instance.category != category:
                del data[field]

        # Fill the legacy permission fields.
        # This block will be deleted once all clients have stopped using these legacy permissions fields.
        if instance.category in [ComputeTask.Category.TASK_TRAIN, ComputeTask.Category.TASK_AGGREGATE]:
            data[TASK_CATEGORY_FIELDS[instance.category]]["model_permissions"] = data["outputs"]["model"]["permissions"]
        elif instance.category == ComputeTask.Category.TASK_COMPOSITE:
            data[TASK_CATEGORY_FIELDS[instance.category]]["head_permissions"] = data["outputs"]["local"]["permissions"]
            data[TASK_CATEGORY_FIELDS[instance.category]]["trunk_permissions"] = data["outputs"]["shared"][
                "permissions"
            ]
        elif instance.category == ComputeTask.Category.TASK_PREDICT:
            data[TASK_CATEGORY_FIELDS[instance.category]]["prediction_permissions"] = data["outputs"]["predictions"][
                "permissions"
            ]

        return data

    def _replace_storage_addresses(self, task):
        super()._replace_storage_addresses(task)

        request = self.context.get("request")
        if not request:
            return task

        # replace in category-dependent relationships
        task_details = task[TASK_CATEGORY_FIELDS[task["category"]]]

        if "data_manager" in task_details and task_details["data_manager"]:
            data_manager = task_details["data_manager"]
            data_manager["description"]["storage_address"] = request.build_absolute_uri(
                reverse("api:data_manager-description", args=[data_manager["key"]])
            )
            data_manager["opener"]["storage_address"] = request.build_absolute_uri(
                reverse("api:data_manager-opener", args=[data_manager["key"]])
            )

        models = task_details.get("models") or []  # field may be set to None
        for model in models:
            if "address" in model and model["address"]:
                model["address"]["storage_address"] = request.build_absolute_uri(
                    reverse("api:model-file", args=[model["key"]])
                )

    class Meta:
        model = ComputeTask
        fields = ComputeTaskSerializer.Meta.fields + [
            "category",
            "aggregate",
            "composite",
            "predict",
            "test",
            "train",
            "parent_task_keys",
        ]


class LegacyComputeTaskWithRelationshipsSerializer(LegacyComputeTaskSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.category in [
            ComputeTask.Category.TASK_TRAIN,
            ComputeTask.Category.TASK_PREDICT,
            ComputeTask.Category.TASK_TEST,
            ComputeTask.Category.TASK_COMPOSITE,
        ]:
            data_manager = DataManager.objects.get(
                key=data[TASK_CATEGORY_FIELDS[instance.category]]["data_manager_key"],
                channel=instance.channel,
            )
            data[TASK_CATEGORY_FIELDS[instance.category]]["data_manager"] = DataManagerSerializer(data_manager).data

        # we need to call this again because this time, there are values for data_manager
        self._replace_storage_addresses(data)

        # parent_tasks
        parent_tasks = ComputeTask.objects.filter(
            key__in=data["parent_task_keys"],
            channel=instance.channel,
        ).order_by("creation_date", "key")
        data["parent_tasks"] = LegacyComputeTaskSerializer(parent_tasks, many=True).data
        for parent_task in data.get("parent_tasks", []):
            self._replace_storage_addresses(parent_task)
        return data

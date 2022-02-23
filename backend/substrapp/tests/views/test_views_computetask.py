import logging
import os
import shutil
import tempfile
from datetime import datetime
from unittest import mock

from django.test import override_settings
from django.urls import reverse
from django.utils.http import urlencode
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

import orchestrator.failure_report_pb2 as failure_report_pb2
from localrep.models import ComputeTask as ComputeTaskRep
from localrep.models import DataManager as DataManagerRep
from localrep.models import Metric as MetricRep
from localrep.models import Performance as PerformanceRep
from localrep.serializers import AlgoSerializer as AlgoRepSerializer
from localrep.serializers import ComputePlanSerializer as ComputePlanRepSerializer
from localrep.serializers import ComputeTaskSerializer as ComputeTaskRepSerializer
from localrep.serializers import DataManagerSerializer as DataManagerRepSerializer
from localrep.serializers import DataSampleSerializer as DataSampleRepSerializer
from localrep.serializers import MetricSerializer as MetricRepSerializer
from orchestrator.client import OrchestratorClient
from substrapp.compute_tasks.errors import ComputeTaskErrorType

from .. import assets
from ..common import AuthenticatedClient
from ..common import internal_server_error_on_exception

MEDIA_ROOT = tempfile.mkdtemp()


class ComputeTaskViewTests(APITestCase):
    client_class = AuthenticatedClient

    def setUp(self):
        if not os.path.exists(MEDIA_ROOT):
            os.makedirs(MEDIA_ROOT)
        self.extra = {"HTTP_SUBSTRA_CHANNEL_NAME": "mychannel", "HTTP_ACCEPT": "application/json;version=0.0"}

        self.logger = logging.getLogger("django.request")
        self.previous_level = self.logger.getEffectiveLevel()
        self.logger.setLevel(logging.ERROR)

        self.algos = assets.get_algos()
        for algo in self.algos:
            serializer = AlgoRepSerializer(data={"channel": "mychannel", **algo})
            serializer.is_valid(raise_exception=True)
            serializer.save()

        self.metrics = assets.get_metrics()
        for metric in self.metrics:
            serializer = MetricRepSerializer(data={"channel": "mychannel", **metric})
            serializer.is_valid(raise_exception=True)
            serializer.save()

        self.data_managers = assets.get_data_managers()
        for data_manager in self.data_managers:
            serializer = DataManagerRepSerializer(data={"channel": "mychannel", **data_manager})
            serializer.is_valid(raise_exception=True)
            serializer.save()

        self.data_samples = assets.get_data_samples()
        for data_sample in self.data_samples:
            serializer = DataSampleRepSerializer(data={"channel": "mychannel", **data_sample})
            serializer.is_valid(raise_exception=True)
            serializer.save()

        self.compute_plans = assets.get_compute_plans()
        for compute_plan in self.compute_plans:
            serializer = ComputePlanRepSerializer(data={"channel": "mychannel", **compute_plan})
            serializer.is_valid(raise_exception=True)
            serializer.save()

        self.train_tasks = assets.get_train_tasks()
        self.test_tasks = assets.get_test_tasks()
        self.composite_tasks = assets.get_composite_tasks()
        for compute_task in self.train_tasks + self.test_tasks + self.composite_tasks:
            data = self.clean_input_data(compute_task)
            serializer = ComputeTaskRepSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

    def clean_input_data(self, compute_task):
        # Missing field from test data
        compute_task["logs_permission"] = {
            "public": True,
            "authorized_ids": [compute_task["owner"]],
        }
        # Unexpected fields from test data
        del compute_task["parent_tasks"]  # only for expand relationships
        if "train" in compute_task:
            del compute_task["train"]["data_manager"]  # only for expand relationships
            if compute_task["status"] != "STATUS_DONE":
                del compute_task["train"]["models"]
        elif "test" in compute_task:
            del compute_task["test"]["data_manager"]  # only for expand relationships
            del compute_task["test"]["metrics"]  # only for expand relationships
            if compute_task["status"] != "STATUS_DONE":
                del compute_task["test"]["perfs"]
        elif "composite" in compute_task:
            del compute_task["composite"]["data_manager"]  # only for expand relationships
            if compute_task["status"] != "STATUS_DONE":
                del compute_task["composite"]["models"]
        data = {"channel": "mychannel", **compute_task}
        if data["error_type"] is None:
            del data["error_type"]
        else:
            data["error_type"] = failure_report_pb2.ErrorType.Name(
                getattr(ComputeTaskErrorType, data["error_type"]).value
            )
        return data

    def tearDown(self):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        self.logger.setLevel(self.previous_level)


@override_settings(
    MEDIA_ROOT=MEDIA_ROOT,
    LEDGER_CHANNELS={"mychannel": {"chaincode": {"name": "mycc"}, "model_export_enabled": True}},
)
class TrainTaskViewTests(ComputeTaskViewTests):
    def setUp(self):
        super().setUp()
        self.url = reverse("substrapp:traintuple-list")

    def test_traintask_list_empty(self):
        ComputeTaskRep.objects.all().delete()
        response = self.client.get(self.url, **self.extra)
        self.assertEqual(response.json(), {"count": 0, "next": None, "previous": None, "results": []})

    def mock_output_models_in_test_data(self, value):
        for train_task in self.train_tasks:
            if train_task["status"] == "STATUS_DONE":
                train_task["train"]["models"] = value

    def test_traintask_list_success(self):
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(self.url, **self.extra)
        self.assertEqual(
            response.json(),
            {"count": len(self.train_tasks), "next": None, "previous": None, "results": self.train_tasks},
        )

    def test_traintask_list_wrong_channel(self):
        extra = {"HTTP_SUBSTRA_CHANNEL_NAME": "yourchannel", "HTTP_ACCEPT": "application/json;version=0.0"}
        response = self.client.get(self.url, **extra)
        self.assertEqual(response.json(), {"count": 0, "next": None, "previous": None, "results": []})

    @internal_server_error_on_exception()
    @mock.patch("substrapp.views.computetask.ComputeTaskViewSet.list", side_effect=Exception("Unexpected error"))
    def test_traintask_list_fail(self, _):
        response = self.client.get(self.url, **self.extra)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_traintask_list_filter(self):
        """Filter traintask on key."""
        key = self.train_tasks[0]["key"]
        params = urlencode({"search": f"traintuple:key:{key}"})
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(response.json(), {"count": 1, "next": None, "previous": None, "results": self.train_tasks[:1]})

    def test_traintask_list_filter_and(self):
        """Filter traintask on key and owner."""
        key, owner = self.train_tasks[0]["key"], self.train_tasks[0]["owner"]
        params = urlencode({"search": f"traintuple:key:{key},traintuple:owner:{owner}"})
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(response.json(), {"count": 1, "next": None, "previous": None, "results": self.train_tasks[:1]})

    def test_traintask_list_filter_or(self):
        """Filter traintask on key_0 or key_1."""
        key_0 = self.train_tasks[0]["key"]
        key_1 = self.train_tasks[1]["key"]
        params = urlencode({"search": f"traintuple:key:{key_0}-OR-traintuple:key:{key_1}"})
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(response.json(), {"count": 2, "next": None, "previous": None, "results": self.train_tasks[:2]})

    def test_traintask_list_filter_or_and(self):
        """Filter traintask on (key_0 and owner_0) or (key_1 and owner_1)."""
        key_0, owner_0 = self.train_tasks[0]["key"], self.train_tasks[0]["owner"]
        key_1, owner_1 = self.train_tasks[1]["key"], self.train_tasks[1]["owner"]
        params = urlencode(
            {
                "search": (
                    f"traintuple:key:{key_0},traintuple:owner:{owner_0}"
                    f"-OR-traintuple:key:{key_1},traintuple:owner:{owner_1}"
                )
            }
        )
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(response.json(), {"count": 2, "next": None, "previous": None, "results": self.train_tasks[:2]})

    @parameterized.expand(
        [
            ("page_size_5_page_1", 5, 1),
            ("page_size_1_page_2", 1, 2),
            ("page_size_2_page_3", 2, 3),
        ]
    )
    def test_traintask_list_pagination_success(self, _, page_size, page):
        params = urlencode({"page_size": page_size, "page": page})
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(f"{self.url}?{params}", **self.extra)
        r = response.json()
        self.assertEqual(r["count"], len(self.train_tasks))
        offset = (page - 1) * page_size
        self.assertEqual(r["results"], self.train_tasks[offset : offset + page_size])

    def test_traintask_cp_list_success(self):
        """List traintasks for a specific compute plan (CPtraintaskViewSet)."""
        # Get a CP with more than one task to have "interesting" results
        compute_plan_key = [cp["key"] for cp in self.compute_plans if cp["task_count"] > 1][0]
        related_task_keys = [ct["key"] for ct in self.train_tasks if ct["compute_plan_key"] == compute_plan_key]
        related_tasks = [ct for ct in self.train_tasks if ct["key"] in related_task_keys]

        url = reverse("substrapp:compute_plan_traintuple-list", args=[compute_plan_key])
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(url, **self.extra)
        self.assertEqual(
            response.json(), {"count": len(related_tasks), "next": None, "previous": None, "results": related_tasks}
        )

    def test_traintask_list_filter_cp_key(self):
        """Filter traintask on key."""
        compute_plan_key = [cp["key"] for cp in self.compute_plans if cp["task_count"] > 1][0]
        related_task_keys = [ct["key"] for ct in self.train_tasks if ct["compute_plan_key"] == compute_plan_key]
        related_tasks = [ct for ct in self.train_tasks if ct["key"] in related_task_keys]

        params = urlencode({"search": f"traintuple:compute_plan_key:{compute_plan_key}"})
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(
            response.json(), {"count": len(related_tasks), "next": None, "previous": None, "results": related_tasks}
        )

    def test_traintask_retrieve(self):
        url = reverse("substrapp:traintuple-detail", args=[self.train_tasks[0]["key"]])
        with mock.patch.object(
            OrchestratorClient, "get_computetask_output_models", return_value=self.train_tasks[0]["train"]["models"]
        ):
            response = self.client.get(url, **self.extra)
        # retrieve view expand relationships
        data_manager = DataManagerRep.objects.get(key=self.train_tasks[0]["train"]["data_manager_key"])
        self.train_tasks[0]["train"]["data_manager"] = DataManagerRepSerializer(data_manager).data
        parent_tasks = ComputeTaskRep.objects.filter(key__in=self.train_tasks[0]["parent_task_keys"]).order_by(
            "creation_date", "key"
        )
        self.train_tasks[0]["parent_tasks"] = ComputeTaskRepSerializer(parent_tasks, many=True).data
        self.assertEqual(response.json(), self.train_tasks[0])

    def test_traintask_retrieve_wrong_channel(self):
        url = reverse("substrapp:traintuple-detail", args=[self.train_tasks[0]["key"]])
        extra = {"HTTP_SUBSTRA_CHANNEL_NAME": "yourchannel", "HTTP_ACCEPT": "application/json;version=0.0"}
        response = self.client.get(url, **extra)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @internal_server_error_on_exception()
    @mock.patch("substrapp.views.computetask.ComputeTaskViewSet.retrieve", side_effect=Exception("Unexpected error"))
    def test_traintask_retrieve_fail(self, _):
        url = reverse("substrapp:traintuple-detail", args=[self.train_tasks[0]["key"]])
        response = self.client.get(url, **self.extra)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)


@override_settings(
    MEDIA_ROOT=MEDIA_ROOT,
    LEDGER_CHANNELS={"mychannel": {"chaincode": {"name": "mycc"}, "model_export_enabled": True}},
)
class TestTaskViewTests(ComputeTaskViewTests):
    def setUp(self):
        super().setUp()
        self.url = reverse("substrapp:testtuple-list")

    def test_testtask_list_empty(self):
        ComputeTaskRep.objects.all().delete()
        response = self.client.get(self.url, **self.extra)
        self.assertEqual(response.json(), {"count": 0, "next": None, "previous": None, "results": []})

    def mock_performances_in_test_data(self, value):
        for test_task in self.test_tasks:
            if test_task["status"] == "STATUS_DONE":
                test_task["test"]["perfs"] = value

    def test_testtask_list_success(self):
        self.mock_performances_in_test_data(value={})
        response = self.client.get(self.url, **self.extra)
        self.assertEqual(
            response.json(),
            {"count": len(self.test_tasks), "next": None, "previous": None, "results": self.test_tasks},
        )

    def test_testtask_list_wrong_channel(self):
        extra = {"HTTP_SUBSTRA_CHANNEL_NAME": "yourchannel", "HTTP_ACCEPT": "application/json;version=0.0"}
        response = self.client.get(self.url, **extra)
        self.assertEqual(response.json(), {"count": 0, "next": None, "previous": None, "results": []})

    @internal_server_error_on_exception()
    @mock.patch("substrapp.views.computetask.ComputeTaskViewSet.list", side_effect=Exception("Unexpected error"))
    def test_testtask_list_fail(self, _):
        response = self.client.get(self.url, **self.extra)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_testtask_list_filter(self):
        """Filter testtask on key."""
        key = self.test_tasks[0]["key"]
        params = urlencode({"search": f"testtuple:key:{key}"})
        self.mock_performances_in_test_data(value={})
        response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(response.json(), {"count": 1, "next": None, "previous": None, "results": self.test_tasks[:1]})

    def test_testtask_list_filter_and(self):
        """Filter testtask on key and owner."""
        key, owner = self.test_tasks[0]["key"], self.test_tasks[0]["owner"]
        params = urlencode({"search": f"testtuple:key:{key},testtuple:owner:{owner}"})
        self.mock_performances_in_test_data(value={})
        response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(response.json(), {"count": 1, "next": None, "previous": None, "results": self.test_tasks[:1]})

    def test_testtask_list_filter_or(self):
        """Filter testtask on key_0 or key_1."""
        key_0 = self.test_tasks[0]["key"]
        key_1 = self.test_tasks[1]["key"]
        params = urlencode({"search": f"testtuple:key:{key_0}-OR-testtuple:key:{key_1}"})
        self.mock_performances_in_test_data(value={})
        response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(response.json(), {"count": 2, "next": None, "previous": None, "results": self.test_tasks[:2]})

    def test_testtask_list_filter_or_and(self):
        """Filter testtask on (key_0 and owner_0) or (key_1 and owner_1)."""
        key_0, owner_0 = self.test_tasks[0]["key"], self.test_tasks[0]["owner"]
        key_1, owner_1 = self.test_tasks[1]["key"], self.test_tasks[1]["owner"]
        params = urlencode(
            {
                "search": (
                    f"testtuple:key:{key_0},testtuple:owner:{owner_0}"
                    f"-OR-testtuple:key:{key_1},testtuple:owner:{owner_1}"
                )
            }
        )
        self.mock_performances_in_test_data(value={})
        response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(response.json(), {"count": 2, "next": None, "previous": None, "results": self.test_tasks[:2]})

    @parameterized.expand(
        [
            ("page_size_5_page_1", 5, 1),
            ("page_size_1_page_2", 1, 2),
            ("page_size_2_page_3", 2, 3),
        ]
    )
    def test_testtask_list_pagination_success(self, _, page_size, page):
        params = urlencode({"page_size": page_size, "page": page})
        self.mock_performances_in_test_data(value={})
        response = self.client.get(f"{self.url}?{params}", **self.extra)
        r = response.json()
        self.assertEqual(r["count"], len(self.test_tasks))
        offset = (page - 1) * page_size
        self.assertEqual(r["results"], self.test_tasks[offset : offset + page_size])

    def test_testtask_cp_list_success(self):
        """List testtasks for a specific compute plan (CPtesttaskViewSet)."""
        # Get a CP with more than one task to have "interesting" results
        compute_plan_key = [cp["key"] for cp in self.compute_plans if cp["task_count"] > 1][0]
        related_task_keys = [ct["key"] for ct in self.test_tasks if ct["compute_plan_key"] == compute_plan_key]
        related_tasks = [ct for ct in self.test_tasks if ct["key"] in related_task_keys]

        url = reverse("substrapp:compute_plan_testtuple-list", args=[compute_plan_key])
        self.mock_performances_in_test_data(value={})
        response = self.client.get(url, **self.extra)
        self.assertEqual(
            response.json(), {"count": len(related_tasks), "next": None, "previous": None, "results": related_tasks}
        )

    def test_testtask_retrieve(self):
        url = reverse("substrapp:testtuple-detail", args=[self.test_tasks[0]["key"]])
        for metric_key, perf_value in self.test_tasks[0]["test"]["perfs"].items():
            PerformanceRep.objects.create(
                compute_task_id=self.test_tasks[0]["key"],
                metric_id=metric_key,
                value=perf_value,
                creation_date=datetime.now(),
                channel="mychannel",
            )
        response = self.client.get(url, **self.extra)
        # retrieve view expand relationships
        data_manager = DataManagerRep.objects.get(key=self.test_tasks[0]["test"]["data_manager_key"])
        self.test_tasks[0]["test"]["data_manager"] = DataManagerRepSerializer(data_manager).data
        metrics = MetricRep.objects.filter(key__in=self.test_tasks[0]["test"]["metric_keys"])
        self.test_tasks[0]["test"]["metrics"] = MetricRepSerializer(metrics, many=True).data
        parent_tasks = ComputeTaskRep.objects.filter(key__in=self.test_tasks[0]["parent_task_keys"]).order_by(
            "creation_date", "key"
        )
        self.test_tasks[0]["parent_tasks"] = ComputeTaskRepSerializer(parent_tasks, many=True).data
        self.assertEqual(response.json(), self.test_tasks[0])
        # self.assertDictEqual(response.json(), self.test_tasks[0])

    def test_testtask_retrieve_wrong_channel(self):
        url = reverse("substrapp:testtuple-detail", args=[self.test_tasks[0]["key"]])
        extra = {"HTTP_SUBSTRA_CHANNEL_NAME": "yourchannel", "HTTP_ACCEPT": "application/json;version=0.0"}
        response = self.client.get(url, **extra)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @internal_server_error_on_exception()
    @mock.patch("substrapp.views.computetask.ComputeTaskViewSet.retrieve", side_effect=Exception("Unexpected error"))
    def test_testtask_retrieve_fail(self, _):
        url = reverse("substrapp:testtuple-detail", args=[self.test_tasks[0]["key"]])
        response = self.client.get(url, **self.extra)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)


@override_settings(
    MEDIA_ROOT=MEDIA_ROOT,
    LEDGER_CHANNELS={"mychannel": {"chaincode": {"name": "mycc"}, "model_export_enabled": True}},
)
class CompositeTaskViewTests(ComputeTaskViewTests):
    def setUp(self):
        super().setUp()
        self.url = reverse("substrapp:composite_traintuple-list")

    def test_compositetask_list_empty(self):
        ComputeTaskRep.objects.all().delete()
        response = self.client.get(self.url, **self.extra)
        self.assertEqual(response.json(), {"count": 0, "next": None, "previous": None, "results": []})

    def mock_output_models_in_test_data(self, value):
        for composite_task in self.composite_tasks:
            if composite_task["status"] == "STATUS_DONE":
                composite_task["composite"]["models"] = value

    def test_compositetask_list_success(self):
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(self.url, **self.extra)
        self.assertEqual(
            response.json(),
            {"count": len(self.composite_tasks), "next": None, "previous": None, "results": self.composite_tasks},
        )

    def test_compositetask_list_wrong_channel(self):
        extra = {"HTTP_SUBSTRA_CHANNEL_NAME": "yourchannel", "HTTP_ACCEPT": "application/json;version=0.0"}
        response = self.client.get(self.url, **extra)
        self.assertEqual(response.json(), {"count": 0, "next": None, "previous": None, "results": []})

    @internal_server_error_on_exception()
    @mock.patch("substrapp.views.computetask.ComputeTaskViewSet.list", side_effect=Exception("Unexpected error"))
    def test_compositetask_list_fail(self, _):
        response = self.client.get(self.url, **self.extra)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_compositetask_list_filter(self):
        """Filter compositetask on key."""
        key = self.composite_tasks[0]["key"]
        params = urlencode({"search": f"composite_traintuple:key:{key}"})
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(
            response.json(), {"count": 1, "next": None, "previous": None, "results": self.composite_tasks[:1]}
        )

    def test_compositetask_list_filter_and(self):
        """Filter compositetask on key and owner."""
        key, owner = self.composite_tasks[0]["key"], self.composite_tasks[0]["owner"]
        params = urlencode({"search": f"composite_traintuple:key:{key},composite_traintuple:owner:{owner}"})
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(
            response.json(), {"count": 1, "next": None, "previous": None, "results": self.composite_tasks[:1]}
        )

    def test_compositetask_list_filter_or(self):
        """Filter compositetask on key_0 or key_1."""
        key_0 = self.composite_tasks[0]["key"]
        key_1 = self.composite_tasks[1]["key"]
        params = urlencode({"search": f"composite_traintuple:key:{key_0}-OR-composite_traintuple:key:{key_1}"})
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(
            response.json(), {"count": 2, "next": None, "previous": None, "results": self.composite_tasks[:2]}
        )

    def test_compositetask_list_filter_or_and(self):
        """Filter compositetask on (key_0 and owner_0) or (key_1 and owner_1)."""
        key_0, owner_0 = self.composite_tasks[0]["key"], self.composite_tasks[0]["owner"]
        key_1, owner_1 = self.composite_tasks[1]["key"], self.composite_tasks[1]["owner"]
        params = urlencode(
            {
                "search": (
                    f"composite_traintuple:key:{key_0},composite_traintuple:owner:{owner_0}"
                    f"-OR-composite_traintuple:key:{key_1},composite_traintuple:owner:{owner_1}"
                )
            }
        )
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(f"{self.url}?{params}", **self.extra)
        self.assertEqual(
            response.json(), {"count": 2, "next": None, "previous": None, "results": self.composite_tasks[:2]}
        )

    @parameterized.expand(
        [
            ("page_size_5_page_1", 5, 1),
            ("page_size_1_page_2", 1, 2),
            ("page_size_2_page_3", 2, 3),
        ]
    )
    def test_compositetask_list_pagination_success(self, _, page_size, page):
        params = urlencode({"page_size": page_size, "page": page})
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(f"{self.url}?{params}", **self.extra)
        r = response.json()
        self.assertEqual(r["count"], len(self.composite_tasks))
        offset = (page - 1) * page_size
        self.assertEqual(r["results"], self.composite_tasks[offset : offset + page_size])

    def test_compositetask_cp_list_success(self):
        """List compositetasks for a specific compute plan (CPcompositetaskViewSet)."""
        # Get a CP with more than one task to have "interesting" results
        compute_plan_key = [cp["key"] for cp in self.compute_plans if cp["task_count"] > 1][0]
        related_task_keys = [ct["key"] for ct in self.composite_tasks if ct["compute_plan_key"] == compute_plan_key]
        related_tasks = [ct for ct in self.composite_tasks if ct["key"] in related_task_keys]

        url = reverse("substrapp:compute_plan_composite_traintuple-list", args=[compute_plan_key])
        self.mock_output_models_in_test_data(value=None)
        with mock.patch.object(OrchestratorClient, "get_computetask_output_models", return_value=None):
            response = self.client.get(url, **self.extra)
        self.assertEqual(
            response.json(), {"count": len(related_tasks), "next": None, "previous": None, "results": related_tasks}
        )

    def test_compositetask_retrieve(self):
        url = reverse("substrapp:composite_traintuple-detail", args=[self.composite_tasks[0]["key"]])
        with mock.patch.object(
            OrchestratorClient,
            "get_computetask_output_models",
            return_value=self.composite_tasks[0]["composite"]["models"],
        ):
            response = self.client.get(url, **self.extra)
        # retrieve view expand relationships
        data_manager = DataManagerRep.objects.get(key=self.composite_tasks[0]["composite"]["data_manager_key"])
        self.composite_tasks[0]["composite"]["data_manager"] = DataManagerRepSerializer(data_manager).data
        parent_tasks = ComputeTaskRep.objects.filter(key__in=self.composite_tasks[0]["parent_task_keys"]).order_by(
            "creation_date", "key"
        )
        self.composite_tasks[0]["parent_tasks"] = ComputeTaskRepSerializer(parent_tasks, many=True).data
        self.assertEqual(response.json(), self.composite_tasks[0])

    def test_compositetask_retrieve_wrong_channel(self):
        url = reverse("substrapp:composite_traintuple-detail", args=[self.composite_tasks[0]["key"]])
        extra = {"HTTP_SUBSTRA_CHANNEL_NAME": "yourchannel", "HTTP_ACCEPT": "application/json;version=0.0"}
        response = self.client.get(url, **extra)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @internal_server_error_on_exception()
    @mock.patch("substrapp.views.computetask.ComputeTaskViewSet.retrieve", side_effect=Exception("Unexpected error"))
    def test_compositetask_retrieve_fail(self, _):
        url = reverse("substrapp:composite_traintuple-detail", args=[self.composite_tasks[0]["key"]])
        response = self.client.get(url, **self.extra)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
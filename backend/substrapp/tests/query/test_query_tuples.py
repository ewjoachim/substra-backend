import os
import shutil
import tempfile
import uuid
from unittest import mock

from django.test import override_settings
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from orchestrator.client import OrchestratorClient
from substrapp.models import Metric

from ..common import AuthenticatedClient
from ..common import get_sample_metric

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(
    MEDIA_ROOT=MEDIA_ROOT,
    LEDGER_CHANNELS={"mychannel": {"chaincode": {"name": "mycc"}, "model_export_enabled": True}},
)
class TraintupleQueryTests(APITestCase):
    client_class = AuthenticatedClient

    def setUp(self):
        if not os.path.exists(MEDIA_ROOT):
            os.makedirs(MEDIA_ROOT)
        (
            self.metric_description,
            self.metric_description_filename,
            self.metric_metrics,
            self.metric_metrics_filename,
        ) = get_sample_metric()

        self.train_data_sample_keys = ["5c1d9cd1-c2c1-082d-de09-21b56d11030c"]
        self.fake_key = "5c1d9cd1-c2c1-082d-de09-21b56d11030c"

    def tearDown(self):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)

    @parameterized.expand([("with_compute_plan", True), ("without_compute_plan", False)])
    def test_add_traintuple_ok(self, _, with_compute_plan):
        # Add associated metric
        description, _, metrics, _ = get_sample_metric()
        Metric.objects.create(description=description, address=metrics)
        # post data
        url = reverse("substrapp:traintuple-list")

        data = {
            "train_data_sample_keys": self.train_data_sample_keys,
            "algo_key": self.fake_key,
            "data_manager_key": self.fake_key,
            "metric_key": self.fake_key,
            "in_models_keys": [self.fake_key],
        }

        if with_compute_plan:
            data["compute_plan_key"] = self.fake_key

        extra = {
            "HTTP_SUBSTRA_CHANNEL_NAME": "mychannel",
            "HTTP_ACCEPT": "application/json;version=0.0",
        }

        with mock.patch.object(OrchestratorClient, "register_tasks") as mregister_task:
            with mock.patch.object(OrchestratorClient, "register_compute_plan") as mregister_compute_plan:
                response = self.client.post(url, data, format="json", **extra)
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                self.assertEqual(mregister_task.call_count, 1)
                if with_compute_plan:
                    self.assertEqual(mregister_compute_plan.call_count, 0)
                else:
                    self.assertEqual(mregister_compute_plan.call_count, 1)

    def test_add_traintuple_ko(self):
        url = reverse("substrapp:traintuple-list")

        data = {"train_data_sample_keys": self.train_data_sample_keys, "model_key": self.fake_key}

        extra = {
            "HTTP_SUBSTRA_CHANNEL_NAME": "mychannel",
            "HTTP_ACCEPT": "application/json;version=0.0",
        }

        response = self.client.post(url, data, format="json", **extra)
        self.assertIn("This field may not be null.", response.json()["message"][0]["algo_key"])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        o = Metric.objects.create(description=self.metric_description, address=self.metric_metrics)
        data = {"metric": o.key}
        response = self.client.post(url, data, format="json", **extra)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


@override_settings(
    MEDIA_ROOT=MEDIA_ROOT,
    LEDGER_CHANNELS={"mychannel": {"chaincode": {"name": "mycc"}, "model_export_enabled": True}},
)
class TesttupleQueryTests(APITestCase):
    client_class = AuthenticatedClient

    def setUp(self):
        if not os.path.exists(MEDIA_ROOT):
            os.makedirs(MEDIA_ROOT)
        (
            self.metric_description,
            self.metric_description_filename,
            self.metric_metrics,
            self.metric_metrics_filename,
        ) = get_sample_metric()
        self.metric_key = "5c1d9cd1-c2c1-082d-de09-21b56d11030c"
        self.test_data_sample_keys = ["5c1d9cd1-c2c1-082d-de09-21b56d11030c"]
        self.fake_key = "5c1d9cd1-c2c1-082d-de09-21b56d11030c"

    def tearDown(self):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)

    @parameterized.expand([("with_data_manager", True), ("without_data_manager", False)])
    def test_add_testtuple_ok(self, _, with_data_manager):
        # Add associated metric
        description, _, metrics, _ = get_sample_metric()
        Metric.objects.create(description=description, address=metrics)
        # post data
        url = reverse("substrapp:testtuple-list")

        data = {
            "algo_key": self.fake_key,
            "metric_key": self.metric_key,
            "test_data_sample_keys": self.test_data_sample_keys,
            "traintuple_key": self.fake_key,
        }

        if with_data_manager:
            data["data_manager_key"] = self.fake_key

        extra = {
            "HTTP_SUBSTRA_CHANNEL_NAME": "mychannel",
            "HTTP_ACCEPT": "application/json;version=0.0",
        }

        with mock.patch.object(OrchestratorClient, "register_tasks", return_value={}), mock.patch.object(
            OrchestratorClient,
            "query_task",
            return_value={"algo": {"key": uuid.uuid4()}, "compute_plan_key": uuid.uuid4()},
        ):
            response = self.client.post(url, data, format="json", **extra)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_testtuple_ko(self):
        url = reverse("substrapp:testtuple-list")

        data = {
            "test_data_sample_keys": self.test_data_sample_keys,
        }

        extra = {
            "HTTP_SUBSTRA_CHANNEL_NAME": "mychannel",
            "HTTP_ACCEPT": "application/json;version=0.0",
        }

        response = self.client.post(url, data, format="json", **extra)
        self.assertIn("This field may not be null.", response.json()["message"][0]["traintuple_key"])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
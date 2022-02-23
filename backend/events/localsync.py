import structlog
from django.conf import settings
from django.db import transaction
from django.utils.dateparse import parse_datetime
from rest_framework.exceptions import ValidationError

import orchestrator.common_pb2 as common_pb2
import orchestrator.computeplan_pb2 as computeplan_pb2
import orchestrator.computetask_pb2 as computetask_pb2
import orchestrator.event_pb2 as event_pb2
import orchestrator.failure_report_pb2 as failure_report_pb2
from localrep.errors import AlreadyExistsError
from orchestrator import client as orc_client
from substrapp.orchestrator import get_orchestrator_client

logger = structlog.get_logger(__name__)


def _on_create_algo_event(event: dict, client: orc_client.OrchestratorClient) -> None:
    """Process create algo event to update local database."""
    logger.debug("Syncing algo create", asset_key=event["asset_key"], event_id=event["id"])

    data = client.query_algo(event["asset_key"])
    _create_algo(event["channel"], data)


def _create_algo(channel: str, data: dict) -> bool:
    from localrep.serializers import AlgoSerializer

    data["channel"] = channel
    serializer = AlgoSerializer(data=data)
    try:
        serializer.save_if_not_exists()
    except AlreadyExistsError:
        logger.debug("Algo already exists", asset_key=data["key"])
        return False
    else:
        return True


def _on_create_computeplan_event(event: dict, client: orc_client.OrchestratorClient) -> None:
    """Process create computeplan event to update local database."""
    logger.debug("Syncing computeplan", asset_key=event["asset_key"], event_id=event["id"])

    data = client.query_compute_plan(event["asset_key"])
    _create_computeplan(event["channel"], data)


def _create_computeplan(channel: str, data: dict) -> bool:
    from localrep.serializers import ComputePlanSerializer

    data["channel"] = channel
    serializer = ComputePlanSerializer(data=data)
    try:
        serializer.save_if_not_exists()
    except AlreadyExistsError:
        logger.debug("ComputePlan already exists", asset_key=data["key"])
        return False
    else:
        return True


def _on_create_computetask_event(event: dict, client: orc_client.OrchestratorClient) -> None:
    """Process create computetask event to update local database."""

    from localrep.models.computeplan import ComputePlan

    logger.debug("Syncing computetask create", asset_key=event["asset_key"], event_id=event["id"])

    data = client.query_task(event["asset_key"])
    _create_computetask(event["channel"], data)

    compute_plan = ComputePlan.objects.get(key=data["compute_plan_key"])
    compute_plan.update_status()


def _create_computetask(
    channel: str, data: dict, start_date: str = None, end_date: str = None, error_type: str = None
) -> bool:
    from localrep.serializers import ComputeTaskSerializer

    data["channel"] = channel
    if start_date is not None:
        data["start_date"] = parse_datetime(start_date)
    if end_date is not None:
        data["end_date"] = parse_datetime(end_date)
    if error_type is not None:
        data["error_type"] = error_type
    # XXX: in case of localsync of MDY dumps, logs_permission won't be provided:
    #      the orchestrator and backend used to generate the dumps are both outdated.
    #      We provide a sensible default: logs are private.
    data.setdefault("logs_permission", {"public": False, "authorized_ids": [data["owner"]]})
    serializer = ComputeTaskSerializer(data=data)
    try:
        serializer.save_if_not_exists()
    except AlreadyExistsError:
        logger.debug("Computetask already exists", asset_key=data["key"])
        return False
    else:
        return True


def _on_update_computetask_event(event: dict, client: orc_client.OrchestratorClient) -> None:
    """Process update computetask event to update local database."""

    from events.dynamic_fields import add_cp_dates_and_duration
    from events.dynamic_fields import add_cp_failed_task
    from events.dynamic_fields import fetch_error_type_from_event
    from events.dynamic_fields import parse_computetask_dates_from_event
    from localrep.models.computeplan import ComputePlan

    logger.debug("Syncing computetask update", asset_key=event["asset_key"], event_id=event["id"])

    data = client.query_task(event["asset_key"])
    candidate_start_date, candidate_end_date = parse_computetask_dates_from_event(event)
    error_type = fetch_error_type_from_event(event, client)
    _update_computetask(data["key"], data["status"], candidate_start_date, candidate_end_date, error_type)

    status = computetask_pb2.ComputeTaskStatus.Value(data["status"])
    category = computetask_pb2.ComputeTaskCategory.Value(data["category"])
    if status != computetask_pb2.STATUS_TODO:
        add_cp_dates_and_duration(data["compute_plan_key"])
    if status == computetask_pb2.STATUS_FAILED:
        # The event processed might not be the first failed one.
        # We cannot use the task data but need to fetch the first failed event from the orchestrator
        add_cp_failed_task(data["compute_plan_key"], client)
    elif status == computetask_pb2.STATUS_DONE and category == computetask_pb2.TASK_TEST:
        _creating_computetask_performances(data["key"], client)

    compute_plan = ComputePlan.objects.get(key=data["compute_plan_key"])
    compute_plan.update_status()


def _update_computetask(key: str, status: str, start_date: str, end_date: str, error_type: str) -> None:
    """Update only mutable fields: status, start_date, end_date, error_type"""
    from localrep.models import ComputeTask

    compute_task = ComputeTask.objects.get(key=key)
    compute_task.status = computetask_pb2.ComputeTaskStatus.Value(status)
    # The computetask start/end date is the timestamp of the first event related to the new status.
    # During a single event sync, we rely on the asset values to deduce if they were previous events.
    # If so, dates are not updated on the asset
    if compute_task.start_date is None and start_date is not None:
        compute_task.start_date = parse_datetime(start_date)
    if compute_task.end_date is None and end_date is not None:
        compute_task.end_date = parse_datetime(end_date)
    if error_type is not None:
        compute_task.error_type = failure_report_pb2.ErrorType.Value(error_type)
    compute_task.save()


def _on_create_datamanager_event(event: dict, client: orc_client.OrchestratorClient) -> None:
    """Process create datamanager event to update local database."""
    logger.debug("Syncing datamanager create", asset_key=event["asset_key"], event_id=event["id"])

    data = client.query_datamanager(event["asset_key"])
    _create_datamanager(event["channel"], data)


def _create_datamanager(channel: str, data: dict) -> bool:
    from localrep.serializers import DataManagerSerializer

    data["channel"] = channel
    # XXX: in case of localsync of MDY dumps, logs_permission won't be provided:
    #      the orchestrator and backend used to generate the dumps are both outdated.
    #      We provide a sensible default: logs are private.
    data.setdefault("logs_permission", {"public": False, "authorized_ids": [data["owner"]]})
    serializer = DataManagerSerializer(data=data)
    try:
        serializer.save_if_not_exists()
    except AlreadyExistsError:
        logger.debug("DataManager already exists", asset_key=data["key"])
        return False
    else:
        return True


def _on_create_datasample_event(event: dict, client: orc_client.OrchestratorClient) -> None:
    """Process create datasample event to update local database."""
    logger.debug("Syncing datasample create", asset_key=event["asset_key"], event_id=event["id"])

    data = client.query_datasample(event["asset_key"])
    _create_datasample(event["channel"], data)


def _create_datasample(channel: str, data: dict) -> bool:
    from localrep.serializers import DataSampleSerializer

    data["channel"] = channel
    serializer = DataSampleSerializer(data=data)
    try:
        serializer.save_if_not_exists()
    except AlreadyExistsError:
        logger.debug("Datasample already exists", asset_key=data["key"])
        return False
    else:
        return True


def _on_update_datasample_event(event: dict, client: orc_client.OrchestratorClient) -> None:
    """Process update datasample event to update local database."""
    logger.debug("Syncing datasample update", asset_key=event["asset_key"], event_id=event["id"])

    data = client.query_datasample(event["asset_key"])
    _update_datasample(data["key"], data["data_manager_keys"])


def _update_datasample(key: str, data_manager_keys: list[str]) -> None:
    """Update only datamanager relations"""
    from localrep.models import DataManager
    from localrep.models import DataSample

    data_managers = DataManager.objects.filter(key__in=data_manager_keys)
    data_sample = DataSample.objects.get(key=key)
    data_sample.data_managers.set(data_managers)
    data_sample.save()


def _on_create_metric_event(event: dict, client: orc_client.OrchestratorClient) -> None:
    """Process create metric event to update local database."""
    logger.debug("Syncing metric create", asset_key=event["asset_key"], event_id=event["id"])

    data = client.query_metric(event["asset_key"])
    _create_metric(event["channel"], data)


def _create_metric(channel: str, data: dict) -> bool:
    from localrep.serializers import MetricSerializer

    data["channel"] = channel
    serializer = MetricSerializer(data=data)
    try:
        serializer.save_if_not_exists()
    except AlreadyExistsError:
        logger.debug("Metric already exists", asset_key=data["key"])
        return False
    else:
        return True


def _create_performance(channel: str, data: dict) -> bool:
    from localrep.serializers import PerformanceSerializer

    data["channel"] = channel
    serializer = PerformanceSerializer(data=data)
    try:
        serializer.save_if_not_exists()
    except ValidationError:
        logger.debug(
            "Performance already exists", compute_task_key=data["compute_task_key"], metric_key=data["metric_key"]
        )
        return False
    else:
        return True


@transaction.atomic
def sync_on_event_message(event: dict, client: orc_client.OrchestratorClient) -> None:
    """Handler to consume event.
    This function is idempotent (can be called in sync and resync mode)
    """
    event_kind = event_pb2.EventKind.Value(event["event_kind"])
    asset_kind = common_pb2.AssetKind.Value(event["asset_kind"])

    if (event_kind, asset_kind) == (event_pb2.EVENT_ASSET_CREATED, common_pb2.ASSET_ALGO):
        _on_create_algo_event(event, client)
    elif (event_kind, asset_kind) == (event_pb2.EVENT_ASSET_CREATED, common_pb2.ASSET_COMPUTE_PLAN):
        _on_create_computeplan_event(event, client)
    elif (event_kind, asset_kind) == (event_pb2.EVENT_ASSET_CREATED, common_pb2.ASSET_DATA_MANAGER):
        _on_create_datamanager_event(event, client)
    elif (event_kind, asset_kind) == (event_pb2.EVENT_ASSET_CREATED, common_pb2.ASSET_DATA_SAMPLE):
        _on_create_datasample_event(event, client)
    elif (event_kind, asset_kind) == (event_pb2.EVENT_ASSET_UPDATED, common_pb2.ASSET_DATA_SAMPLE):
        _on_update_datasample_event(event, client)
    elif (event_kind, asset_kind) == (event_pb2.EVENT_ASSET_CREATED, common_pb2.ASSET_METRIC):
        _on_create_metric_event(event, client)
    elif (event_kind, asset_kind) == (event_pb2.EVENT_ASSET_CREATED, common_pb2.ASSET_COMPUTE_TASK):
        _on_create_computetask_event(event, client)
    elif (event_kind, asset_kind) == (event_pb2.EVENT_ASSET_UPDATED, common_pb2.ASSET_COMPUTE_TASK):
        _on_update_computetask_event(event, client)
    else:
        logger.debug("Nothing to sync", event_kind=event["event_kind"], asset_kind=event["asset_kind"])


def resync_algos(client: orc_client.OrchestratorClient):
    logger.info("Resyncing algos")
    algos = client.query_algos()  # TODO: Add filter on last_modification_date
    nb_new_assets = 0
    nb_skipped_assets = 0

    for data in algos:
        is_created = _create_algo(client.channel_name, data)
        if is_created:
            logger.debug("Created new algo", asset_key=data["key"])
            nb_new_assets += 1
        else:
            logger.debug("Skipped algo", asset_key=data["key"])
            nb_skipped_assets += 1

    logger.info("Done resync algos", nb_new_assets=nb_new_assets, nb_skipped_assets=nb_skipped_assets)


def resync_metrics(client: orc_client.OrchestratorClient):
    logger.info("Resyncing metrics")
    metrics = client.query_metrics()  # TODO: Add filter on last_modification_date
    nb_new_assets = 0
    nb_skipped_assets = 0

    for data in metrics:
        is_created = _create_metric(client.channel_name, data)
        if is_created:
            logger.debug("Created new metric", asset_key=data["key"])
            nb_new_assets += 1
        else:
            logger.debug("Skipped metric", asset_key=data["key"])
            nb_skipped_assets += 1

    logger.info("Done resync metrics", nb_new_assets=nb_new_assets, nb_skipped_assets=nb_skipped_assets)


def resync_datamanagers(client: orc_client.OrchestratorClient):
    logger.info("Resyncing datamanagers")
    datamanagers = client.query_datamanagers()  # TODO: Add filter on last_modification_date
    nb_new_assets = 0
    nb_skipped_assets = 0

    for data in datamanagers:
        is_created = _create_datamanager(client.channel_name, data)
        if is_created:
            logger.debug("Created new datamanager", asset_key=data["key"])
            nb_new_assets += 1
        else:
            logger.debug("Skipped datamanager", asset_key=data["key"])
            nb_skipped_assets += 1

    logger.info("Done resync datamanagers", nb_new_assets=nb_new_assets, nb_skipped_assets=nb_skipped_assets)


def resync_datasamples(client: orc_client.OrchestratorClient):
    logger.info("Resyncing datasamples")
    datasamples = client.query_datasamples()  # TODO: Add filter on last_modification_date
    nb_new_assets = 0
    nb_updated_assets = 0

    for data in datasamples:
        is_created = _create_datasample(client.channel_name, data)
        if is_created:
            logger.debug("Created new datasample", asset_key=data["key"])
            nb_new_assets += 1
        else:
            _update_datasample(data["key"], data["data_manager_keys"])
            logger.debug("Updated datasample", asset_key=data["key"])
            nb_updated_assets += 1

    logger.info("Done resync datasamples", nb_new_assets=nb_new_assets, nb_updated_assets=nb_updated_assets)


def resync_computeplans(client: orc_client.OrchestratorClient):
    from events.dynamic_fields import add_cp_dates_and_duration
    from events.dynamic_fields import add_cp_failed_task
    from localrep.models.computeplan import ComputePlan

    logger.info("Resyncing computeplans")

    computeplans = client.query_compute_plans()  # TODO: Add filter on last_modification_date
    nb_new_assets = 0
    nb_skipped_assets = 0

    for data in computeplans:
        is_created = _create_computeplan(client.channel_name, data)
        status = computeplan_pb2.ComputePlanStatus.Value(data["status"])
        if status != computeplan_pb2.PLAN_STATUS_TODO:
            add_cp_dates_and_duration(data["key"])
        if status == computeplan_pb2.PLAN_STATUS_FAILED:
            add_cp_failed_task(data["key"], client)
        if is_created:
            logger.debug("Created new computeplan", asset_key=data["key"])
            nb_new_assets += 1
        else:
            logger.debug("Skipped computeplan", asset_key=data["key"])
            nb_skipped_assets += 1
        compute_plan = ComputePlan.objects.get(key=data["key"])
        compute_plan.update_status()
    logger.info("Done resync computeplans", nb_new_assets=nb_new_assets, nb_skipped_assets=nb_skipped_assets)


def _creating_computetask_performances(compute_task_key: str, client: orc_client.OrchestratorClient) -> None:
    logger.info("creating task performances ", task_key=compute_task_key)
    performances = client.get_compute_task_performances(compute_task_key)
    nb_new_assets = 0
    nb_skipped_assets = 0

    for data in performances:
        is_created = _create_performance(client.channel_name, data)
        if is_created:
            logger.debug(
                "Created new performance", compute_task_key=data["compute_task_key"], metric_key=data["metric_key"]
            )
            nb_new_assets += 1
        else:
            logger.debug(
                "Skipped performance", compute_task_key=data["compute_task_key"], metric_key=data["metric_key"]
            )
            nb_skipped_assets += 1

    logger.info(
        "Done creating performances for task",
        task_key=compute_task_key,
        nb_new_assets=nb_new_assets,
        nb_skipped_assets=nb_skipped_assets,
    )


def resync_computetasks(client: orc_client.OrchestratorClient):
    from events.dynamic_fields import fetch_error_type_from_event
    from events.dynamic_fields import parse_computetask_dates_from_event

    logger.info("Resyncing computetasks")
    computetasks = client.query_tasks()  # TODO: Add filter on last_modification_date
    nb_new_assets = 0
    nb_updated_assets = 0

    for data in computetasks:
        start_date, end_date, error_type = None, None, None
        events = client.query_events(
            asset_key=data["key"],
            asset_kind=common_pb2.ASSET_COMPUTE_TASK,
            event_kind=event_pb2.EVENT_ASSET_UPDATED,
        )
        for event in events:
            candidate_start_date, candidate_end_date = parse_computetask_dates_from_event(event)
            # The computetask start/end date is the timestamp of the first event related to the new status
            if start_date is None and candidate_start_date is not None:
                start_date = candidate_start_date
            if end_date is None and candidate_end_date is not None:
                end_date = candidate_end_date
            if error_type is None:
                error_type = fetch_error_type_from_event(event, client)

        is_created = _create_computetask(client.channel_name, data, start_date, end_date, error_type)
        if is_created:
            logger.debug("Created new computetask", asset_key=data["key"])
            nb_new_assets += 1
        else:
            _update_computetask(data["key"], data["status"], start_date, end_date, error_type)
            logger.debug("Updated computetask", asset_key=data["key"])
            nb_updated_assets += 1
        if data["category"] == computetask_pb2.ComputeTaskCategory.Name(computetask_pb2.TASK_TEST) and data[
            "status"
        ] in [
            computetask_pb2.ComputeTaskStatus.Name(computetask_pb2.STATUS_DOING),
            computetask_pb2.ComputeTaskStatus.Name(computetask_pb2.STATUS_DONE),
        ]:
            _creating_computetask_performances(data["key"], client)

    logger.info("Done resync computetasks", nb_new_assets=nb_new_assets, nb_updated_assets=nb_updated_assets)


def resync() -> None:
    """Resync the local asset representation.
    Fetch all assets from the orchestrator that are not present locally in the backend.
    """
    logger.info("Resyncing local representation")

    for channel_name in settings.LEDGER_CHANNELS.keys():
        logger.info("Resyncing for channel", channel=channel_name)
        with get_orchestrator_client(channel_name) as client:
            resync_algos(client)
            resync_metrics(client)
            resync_datamanagers(client)
            resync_datasamples(client)
            resync_computeplans(client)
            resync_computetasks(client)

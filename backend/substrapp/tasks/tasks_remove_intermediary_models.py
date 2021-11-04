import structlog
from typing import List
from backend.celery import app
from substrapp.orchestrator import get_orchestrator_client
from substrapp.compute_tasks.asset_buffer import delete_models_from_buffer

logger = structlog.get_logger(__name__)


def queue_remove_intermediary_models_from_db(channel_name, model_keys):
    # the task can run on any worker
    from substrapp.task_routing import get_generic_worker_queue
    worker_queue = get_generic_worker_queue()

    remove_intermediary_models_from_db.apply_async((channel_name, model_keys), queue=worker_queue)


@app.task(ignore_result=False)
def remove_intermediary_models_from_db(channel_name: str, model_keys: List[str]) -> None:
    """
    Remove model from db.
    Disable model in orchestrator.
    """
    from substrapp.models import Model

    models = Model.objects.filter(key__in=model_keys, validated=True)
    filtered_model_keys = [str(model.key) for model in models]
    models.delete()

    if filtered_model_keys:

        with get_orchestrator_client(channel_name) as client:
            for model_key in filtered_model_keys:
                client.disable_model(model_key)

        logger.info("Delete intermediary models", model_keys=", ".join(filtered_model_keys))


# This task is routed to run on the broadcast exchange
# Each worker is listening to the broadcast queue. All running worker will perform this task.
# Mutliple tasks with the same task_id are created in the db
# With ignore_result set to true, we ignore the result of the task as the different task state
# result might be conflicting.
# See https://docs.celeryproject.org/en/stable/userguide/routing.html#Broadcast&Results
@app.task(ignore_result=True)
def remove_intermediary_models_from_buffer(model_key: str) -> None:
    delete_models_from_buffer([model_key])
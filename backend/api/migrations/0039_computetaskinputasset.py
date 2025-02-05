# Generated by Django 4.0.7 on 2022-09-21 10:10

import django.db.models.deletion
from django.db import migrations
from django.db import models


def create_input_assets(apps, schema_editor):
    ComputeTask = apps.get_model("api", "ComputeTask")  # noqa: N806
    ComputeTaskOutput = apps.get_model("api", "ComputeTaskOutput")  # noqa: N806
    ComputeTaskInputAsset = apps.get_model("api", "ComputeTaskInputAsset")  # noqa: N806
    for task in ComputeTask.objects.all():
        input_kinds = {algo_input.identifier: algo_input.kind for algo_input in task.algo.inputs.all()}
        for task_input in task.inputs.all():
            if task_input.asset_key:
                ComputeTaskInputAsset.objects.create(
                    channel=task_input.channel,
                    task_input=task_input,
                    asset_key=task_input.asset_key,
                    asset_kind=input_kinds[task_input.identifier],
                )
            elif task_input.parent_task_key:
                task_output = ComputeTaskOutput.objects.get(
                    task=task_input.parent_task_key,
                    identifier=task_input.parent_task_output_identifier,
                )
                task_output_asset = task_output.assets.first()
                if task_output_asset:
                    ComputeTaskInputAsset.objects.create(
                        channel=task_input.channel,
                        task_input=task_input,
                        asset_key=task_output_asset.asset_key,
                        asset_kind=input_kinds[task_input.identifier],
                    )


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0038_remove_algo_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="ComputeTaskInputAsset",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "asset_kind",
                    models.CharField(
                        choices=[
                            ("ASSET_DATA_SAMPLE", "Asset Data Sample"),
                            ("ASSET_DATA_MANAGER", "Asset Data Manager"),
                            ("ASSET_MODEL", "Asset Model"),
                        ],
                        max_length=64,
                    ),
                ),
                ("asset_key", models.UUIDField()),
                ("channel", models.CharField(max_length=100)),
                (
                    "task_input",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, related_name="asset", to="api.computetaskinput"
                    ),
                ),
            ],
        ),
        migrations.RunPython(create_input_assets),
    ]

# Generated by Django 4.0.3 on 2022-04-21 15:23

import django.db.models.deletion
from django.db import migrations
from django.db import models


def convert_address(apps, schema_editor):
    metric_model = apps.get_model("api", "metric")
    for metric in metric_model.objects.all():
        metric.description_address = metric.description_address.replace("/metric/", "/algo/")
        metric.algorithm_address = metric.algorithm_address.replace("/metric/", "/algo/").replace("/metrics/", "/file/")
        metric.save()


def copy_from_metric_to_algo(apps, schema_editor):
    metric_model = apps.get_model("api", "metric")
    algo_model = apps.get_model("api", "algo")

    for metric in metric_model.objects.all().values():
        algo_model.objects.create(**metric)


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_taskdatasamples_remove_computetask_data_samples_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="metric",
            name="category",
            field=models.IntegerField(
                choices=[
                    (0, "ALGO_UNKNOWN"),
                    (1, "ALGO_SIMPLE"),
                    (2, "ALGO_AGGREGATE"),
                    (3, "ALGO_COMPOSITE"),
                    (4, "ALGO_METRIC"),
                ],
                default=4,
            ),
        ),
        migrations.RenameField(model_name="metric", old_name="metric_address", new_name="algorithm_address"),
        migrations.RenameField(model_name="metric", old_name="metric_checksum", new_name="algorithm_checksum"),
        migrations.RunPython(convert_address),
        migrations.RunPython(copy_from_metric_to_algo),
        migrations.AlterField(
            model_name="computetask",
            name="metrics",
            field=models.ManyToManyField(related_name="test_tasks", to="api.algo"),
        ),
        migrations.AlterField(
            model_name="performance",
            name="metric",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, related_name="performances", to="api.algo"
            ),
        ),
        migrations.DeleteModel(
            name="Metric",
        ),
    ]

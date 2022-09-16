# Generated by Django 4.0.4 on 2022-06-29 23:45

from django.db import migrations

import api


def migrate_test_tasks(apps, schema_editor):
    # Set algo_key to metrics_keys[0]
    ComputeTask = apps.get_model("api", "ComputeTask")  # noqa: N806
    for task in ComputeTask.objects.filter(category=api.models.ComputeTask.Category.TASK_TEST):
        task.algo = task.metrics.all()[0]
        task.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0020_channelorganization_address"),
    ]

    operations = [
        migrations.RunPython(migrate_test_tasks),
    ]
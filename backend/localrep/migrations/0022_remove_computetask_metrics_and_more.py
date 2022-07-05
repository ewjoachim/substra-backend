# Generated by Django 4.0.4 on 2022-06-29 23:46

import django.contrib.postgres.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("localrep", "0021_data_migration_test_tasks"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="computetask",
            name="metrics",
        ),
        migrations.AddField(
            model_name="computetask",
            name="prediction_permissions_download_authorized_ids",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=1024), null=True, size=100
            ),
        ),
        migrations.AddField(
            model_name="computetask",
            name="prediction_permissions_download_public",
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name="computetask",
            name="prediction_permissions_process_authorized_ids",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=1024), null=True, size=100
            ),
        ),
        migrations.AddField(
            model_name="computetask",
            name="prediction_permissions_process_public",
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name="computeplan",
            name="failed_task_category",
            field=models.CharField(
                choices=[
                    ("TASK_TRAIN", "Task Train"),
                    ("TASK_AGGREGATE", "Task Aggregate"),
                    ("TASK_COMPOSITE", "Task Composite"),
                    ("TASK_PREDICT", "Task Predict"),
                    ("TASK_TEST", "Task Test"),
                ],
                max_length=64,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="computetask",
            name="category",
            field=models.CharField(
                choices=[
                    ("TASK_TRAIN", "Task Train"),
                    ("TASK_AGGREGATE", "Task Aggregate"),
                    ("TASK_COMPOSITE", "Task Composite"),
                    ("TASK_PREDICT", "Task Predict"),
                    ("TASK_TEST", "Task Test"),
                ],
                max_length=64,
            ),
        ),
    ]

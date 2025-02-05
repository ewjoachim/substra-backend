# Generated by Django 4.0.7 on 2022-10-10 07:20

from django.db import migrations
from django.db import models

import substrapp.models.compute_task_failure_report
import substrapp.models.datamanager
import substrapp.models.function
import substrapp.storages.minio


class Migration(migrations.Migration):

    dependencies = [
        ("substrapp", "0011_workerlastevent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="algo",
            name="description",
            field=models.FileField(
                max_length=500,
                storage=substrapp.storages.minio.MinioStorage("substra-algo"),
                upload_to=substrapp.models.function.upload_to,
            ),
        ),
        migrations.AlterField(
            model_name="algo",
            name="file",
            field=models.FileField(
                max_length=500,
                storage=substrapp.storages.minio.MinioStorage("substra-algo"),
                upload_to=substrapp.models.function.upload_to,
            ),
        ),
        migrations.AlterField(
            model_name="computetaskfailurereport",
            name="logs",
            field=models.FileField(
                max_length=36,
                storage=substrapp.storages.minio.MinioStorage("substra-compute-task-logs"),
                upload_to=substrapp.models.compute_task_failure_report._upload_to,
            ),
        ),
        migrations.AlterField(
            model_name="datamanager",
            name="data_opener",
            field=models.FileField(
                max_length=500,
                storage=substrapp.storages.minio.MinioStorage("substra-datamanager"),
                upload_to=substrapp.models.datamanager.upload_to,
            ),
        ),
        migrations.AlterField(
            model_name="datamanager",
            name="description",
            field=models.FileField(
                max_length=500,
                storage=substrapp.storages.minio.MinioStorage("substra-datamanager"),
                upload_to=substrapp.models.datamanager.upload_to,
            ),
        ),
    ]

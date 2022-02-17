# Generated by Django 4.0 on 2022-01-24 10:00

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("localrep", "0002_datamanager_datasample"),
    ]

    operations = [
        migrations.CreateModel(
            name="ComputePlan",
            fields=[
                ("key", models.UUIDField(primary_key=True, serialize=False)),
                ("owner", models.CharField(max_length=100)),
                ("delete_intermediary_models", models.BooleanField(null=True)),
                ("tag", models.CharField(blank=True, max_length=100)),
                ("creation_date", models.DateTimeField()),
                ("metadata", models.JSONField(null=True)),
                ("channel", models.CharField(max_length=100)),
            ],
        ),
    ]
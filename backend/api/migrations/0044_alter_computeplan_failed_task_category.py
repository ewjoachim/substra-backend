# Generated by Django 4.0.7 on 2023-01-13 16:07

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0043_remove_computetask_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="computeplan",
            name="failed_task_category",
            field=models.CharField(default="TASK_UNKNOWN", max_length=64, null=True),
        ),
    ]

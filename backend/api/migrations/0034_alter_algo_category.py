# Generated by Django 4.0.7 on 2022-09-16 14:26

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0033_computetaskoutputasset"),
    ]

    operations = [
        migrations.AlterField(
            model_name="algo",
            name="category",
            field=models.CharField(
                choices=[
                    ("ALGO_SIMPLE", "Algo Simple"),
                    ("ALGO_AGGREGATE", "Algo Aggregate"),
                    ("ALGO_COMPOSITE", "Algo Composite"),
                    ("ALGO_METRIC", "Algo Metric"),
                    ("ALGO_PREDICT", "Algo Predict"),
                    ("ALGO_UNKNOWN", "Algo Unknown"),
                ],
                max_length=64,
            ),
        ),
    ]

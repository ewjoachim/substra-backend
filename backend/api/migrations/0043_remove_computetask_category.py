# Generated by Django 4.0.7 on 2022-10-10 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0042_computeplan_creator"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="computetask",
            name="category",
        ),
    ]

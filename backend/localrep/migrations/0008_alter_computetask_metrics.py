# Generated by Django 4.0.3 on 2022-04-07 12:49

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("localrep", "0007_channelnode_channelnode_unique_id_for_channel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="computetask",
            name="metrics",
            field=models.ManyToManyField(related_name="compute_tasks", to="localrep.metric"),
        ),
    ]

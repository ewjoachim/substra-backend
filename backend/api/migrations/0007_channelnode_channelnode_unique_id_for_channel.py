# Generated by Django 4.0.1 on 2022-03-07 16:33

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_computetask_logs_address_computetask_logs_checksum_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChannelNode",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("node_id", models.CharField(max_length=64)),
                ("creation_date", models.DateTimeField()),
                ("channel", models.CharField(max_length=100)),
            ],
            options={
                "ordering": ["node_id"],
            },
        ),
        migrations.AddConstraint(
            model_name="channelnode",
            constraint=models.UniqueConstraint(fields=("node_id", "channel"), name="unique_id_for_channel"),
        ),
    ]
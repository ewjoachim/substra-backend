# Generated by Django 4.0.6 on 2022-08-08 16:04

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("localrep", "0030_computetaskoutput_transient"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskProfiling",
            fields=[
                (
                    "compute_task",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="task_profiling",
                        serialize=False,
                        to="localrep.computetask",
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["creation_date"],
            },
        ),
        migrations.CreateModel(
            name="ProfilingStep",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("step", models.CharField(max_length=100)),
                ("duration", models.DurationField()),
                (
                    "compute_task_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="execution_rundown",
                        to="localrep.taskprofiling",
                    ),
                ),
            ],
            options={
                "ordering": ["step"],
                "unique_together": {("compute_task_profile", "step")},
            },
        ),
    ]

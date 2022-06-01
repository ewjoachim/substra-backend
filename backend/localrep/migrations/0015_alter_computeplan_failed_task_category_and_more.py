# Generated by Django 4.0.4 on 2022-05-11 09:56

from django.db import migrations
from django.db import models


def migrate_computetasks(apps, schema_editor):
    category_mapping = {
        1: "TASK_TRAIN",
        2: "TASK_AGGREGATE",
        3: "TASK_COMPOSITE",
        4: "TASK_TEST",
    }
    status_mapping = {
        1: "STATUS_WAITING",
        2: "STATUS_TODO",
        3: "STATUS_DOING",
        4: "STATUS_DONE",
        5: "STATUS_CANCELED",
        6: "STATUS_FAILED",
    }
    error_type_mapping = {
        1: "ERROR_TYPE_BUILD",
        2: "ERROR_TYPE_EXECUTION",
        3: "ERROR_TYPE_INTERNAL",
    }
    computetask_model = apps.get_model("localrep", "computetask")
    for computetask_instance in computetask_model.objects.all():
        computetask_instance.category = category_mapping[computetask_instance.category_int]
        computetask_instance.status = status_mapping[computetask_instance.status_int]
        computetask_instance.error_type = error_type_mapping.get(computetask_instance.error_type_int)
        computetask_instance.save()


def migrate_computeplans(apps, schema_editor):
    status_mapping = {
        0: "PLAN_STATUS_UNKNOWN",
        1: "PLAN_STATUS_WAITING",
        2: "PLAN_STATUS_TODO",
        3: "PLAN_STATUS_DOING",
        4: "PLAN_STATUS_DONE",
        5: "PLAN_STATUS_CANCELED",
        6: "PLAN_STATUS_FAILED",
    }
    failed_task_category_mapping = {
        1: "TASK_TRAIN",
        2: "TASK_AGGREGATE",
        3: "TASK_COMPOSITE",
        4: "TASK_TEST",
    }
    computeplan_model = apps.get_model("localrep", "computeplan")
    for computeplan_instance in computeplan_model.objects.all():
        computeplan_instance.status = status_mapping[computeplan_instance.status_int]
        computeplan_instance.failed_task_category = failed_task_category_mapping.get(
            computeplan_instance.failed_task_category_int
        )
        computeplan_instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ("localrep", "0014_alter_model_category"),
    ]

    operations = [
        # temporary fields used to migrate data
        migrations.RenameField(
            model_name="computetask",
            old_name="category",
            new_name="category_int",
        ),
        migrations.RenameField(
            model_name="computetask",
            old_name="status",
            new_name="status_int",
        ),
        migrations.RenameField(
            model_name="computetask",
            old_name="error_type",
            new_name="error_type_int",
        ),
        migrations.RenameField(
            model_name="computeplan",
            old_name="status",
            new_name="status_int",
        ),
        migrations.RenameField(
            model_name="computeplan",
            old_name="failed_task_category",
            new_name="failed_task_category_int",
        ),
        migrations.AddField(
            model_name="computetask",
            name="category",
            field=models.CharField(
                choices=[
                    ("TASK_TRAIN", "Task Train"),
                    ("TASK_AGGREGATE", "Task Aggregate"),
                    ("TASK_COMPOSITE", "Task Composite"),
                    ("TASK_TEST", "Task Test"),
                ],
                max_length=64,
                default="TEMPORARY_MIGRATION_VALUE",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="computetask",
            name="status",
            field=models.CharField(
                choices=[
                    ("STATUS_WAITING", "Status Waiting"),
                    ("STATUS_TODO", "Status Todo"),
                    ("STATUS_DOING", "Status Doing"),
                    ("STATUS_DONE", "Status Done"),
                    ("STATUS_CANCELED", "Status Canceled"),
                    ("STATUS_FAILED", "Status Failed"),
                ],
                max_length=64,
                default="TEMPORARY_MIGRATION_VALUE",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="computetask",
            name="error_type",
            field=models.CharField(
                choices=[
                    ("ERROR_TYPE_BUILD", "Error Type Build"),
                    ("ERROR_TYPE_EXECUTION", "Error Type Execution"),
                    ("ERROR_TYPE_INTERNAL", "Error Type Internal"),
                ],
                max_length=64,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="computeplan",
            name="status",
            field=models.CharField(
                choices=[
                    ("PLAN_STATUS_UNKNOWN", "Plan Status Unknown"),
                    ("PLAN_STATUS_WAITING", "Plan Status Waiting"),
                    ("PLAN_STATUS_TODO", "Plan Status Todo"),
                    ("PLAN_STATUS_DOING", "Plan Status Doing"),
                    ("PLAN_STATUS_DONE", "Plan Status Done"),
                    ("PLAN_STATUS_CANCELED", "Plan Status Canceled"),
                    ("PLAN_STATUS_FAILED", "Plan Status Failed"),
                ],
                max_length=64,
                default="TEMPORARY_MIGRATION_VALUE",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="computeplan",
            name="failed_task_category",
            field=models.CharField(
                choices=[
                    ("TASK_TRAIN", "Task Train"),
                    ("TASK_AGGREGATE", "Task Aggregate"),
                    ("TASK_COMPOSITE", "Task Composite"),
                    ("TASK_TEST", "Task Test"),
                ],
                max_length=64,
                null=True,
            ),
        ),
        migrations.RunPython(migrate_computetasks),
        migrations.RunPython(migrate_computeplans),
        migrations.RemoveField(
            model_name="computetask",
            name="category_int",
        ),
        migrations.RemoveField(
            model_name="computetask",
            name="status_int",
        ),
        migrations.RemoveField(
            model_name="computetask",
            name="error_type_int",
        ),
        migrations.RemoveField(
            model_name="computeplan",
            name="status_int",
        ),
        migrations.RemoveField(
            model_name="computeplan",
            name="failed_task_category_int",
        ),
    ]
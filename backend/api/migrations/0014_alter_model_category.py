# Generated by Django 4.0.4 on 2022-05-11 09:09

from django.db import migrations
from django.db import models


def migrate_data(apps, schema_editor):
    category_mapping = {
        1: "MODEL_SIMPLE",
        2: "MODEL_HEAD",
    }
    model_model = apps.get_model("api", "model")
    for model_instance in model_model.objects.all():
        model_instance.category = category_mapping[model_instance.category_int]
        model_instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0013_computeplan_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="model",
            old_name="category",
            new_name="category_int",
        ),
        migrations.AddField(
            model_name="model",
            name="category",
            field=models.CharField(
                choices=[
                    ("MODEL_SIMPLE", "Model Simple"),
                    ("MODEL_HEAD", "Model Head"),
                ],
                max_length=64,
                default="TEMPORARY_MIGRATION_VALUE",
            ),
            preserve_default=False,
        ),
        migrations.RunPython(migrate_data),
        migrations.RemoveField(
            model_name="model",
            name="category_int",
        ),
    ]

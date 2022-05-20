# Generated by Django 4.0.4 on 2022-05-18 08:43

import django.db.models.deletion
from django.db import migrations
from django.db import models

ALGO_INPUTS_PER_CATEGORY = {
    "ALGO_SIMPLE": {
        "datasamples": {"kind": "ASSET_DATA_SAMPLE", "multiple": True, "optional": False},
        "model": {"kind": "ASSET_MODEL", "multiple": False, "optional": True},
        "opener": {"kind": "ASSET_DATA_MANAGER", "multiple": False, "optional": False},
    },
    "ALGO_AGGREGATE": {
        "model": {"kind": "ASSET_MODEL", "multiple": True, "optional": False},
    },
    "ALGO_COMPOSITE": {
        "datasamples": {"kind": "ASSET_DATA_SAMPLE", "multiple": True, "optional": False},
        "local": {"kind": "ASSET_MODEL", "multiple": False, "optional": True},
        "opener": {"kind": "ASSET_DATA_MANAGER", "multiple": False, "optional": False},
        "shared": {"kind": "ASSET_MODEL", "multiple": False, "optional": True},
    },
    "ALGO_METRIC": {
        "datasamples": {"kind": "ASSET_DATA_SAMPLE", "multiple": True, "optional": False},
        "opener": {"kind": "ASSET_DATA_MANAGER", "multiple": False, "optional": False},
        "predictions": {"kind": "ASSET_MODEL", "multiple": False, "optional": False},
    },
}


ALGO_OUTPUTS_PER_CATEGORY = {
    "ALGO_SIMPLE": {
        "model": {"kind": "ASSET_MODEL", "multiple": False},
    },
    "ALGO_AGGREGATE": {
        "model": {"kind": "ASSET_MODEL", "multiple": False},
    },
    "ALGO_COMPOSITE": {
        "local": {"kind": "ASSET_MODEL", "multiple": False},
        "shared": {"kind": "ASSET_MODEL", "multiple": False},
    },
    "ALGO_METRIC": {
        "performance": {"kind": "ASSET_PERFORMANCE", "multiple": False},
    },
}


def migrate_algo(apps, schema_editor):
    algo_model = apps.get_model("localrep", "algo")
    input_model = apps.get_model("localrep", "algoinput")
    output_model = apps.get_model("localrep", "algooutput")

    for algo_instance in algo_model.objects.all():
        input_model.objects.bulk_create(
            [
                input_model(algo=algo_instance, identifier=identifier, **input_data)
                for identifier, input_data in ALGO_INPUTS_PER_CATEGORY[algo_instance.category].items()
            ]
        )
        output_model.objects.bulk_create(
            [
                output_model(algo=algo_instance, identifier=identifier, **output_data)
                for identifier, output_data in ALGO_OUTPUTS_PER_CATEGORY[algo_instance.category].items()
            ]
        )


class Migration(migrations.Migration):

    dependencies = [
        ("localrep", "0015_alter_computeplan_failed_task_category_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AlgoOutput",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("identifier", models.CharField(max_length=100)),
                (
                    "kind",
                    models.CharField(
                        choices=[("ASSET_MODEL", "Asset Model"), ("ASSET_PERFORMANCE", "Asset Performance")],
                        max_length=64,
                    ),
                ),
                ("multiple", models.BooleanField(default=False)),
                (
                    "algo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="outputs", to="localrep.algo"
                    ),
                ),
            ],
            options={
                "ordering": ["identifier"],
                "unique_together": {("algo", "identifier")},
            },
        ),
        migrations.CreateModel(
            name="AlgoInput",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("identifier", models.CharField(max_length=100)),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("ASSET_DATA_SAMPLE", "Asset Data Sample"),
                            ("ASSET_DATA_MANAGER", "Asset Data Manager"),
                            ("ASSET_MODEL", "Asset Model"),
                        ],
                        max_length=64,
                    ),
                ),
                ("optional", models.BooleanField(default=False)),
                ("multiple", models.BooleanField(default=False)),
                (
                    "algo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="inputs", to="localrep.algo"
                    ),
                ),
            ],
            options={
                "ordering": ["identifier"],
                "unique_together": {("algo", "identifier")},
            },
        ),
        migrations.RunPython(migrate_algo),
    ]

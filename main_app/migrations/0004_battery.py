# Generated by Django 4.2.3 on 2023-08-03 23:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0003_rename_actions_maint_action"),
    ]

    operations = [
        migrations.CreateModel(
            name="Battery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Connector", models.CharField(max_length=10)),
                ("MaH", models.IntegerField()),
                ("Cells", models.CharField(max_length=5)),
            ],
        ),
    ]

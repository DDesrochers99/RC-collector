# Generated by Django 4.2.3 on 2023-08-03 20:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0002_maint"),
    ]

    operations = [
        migrations.RenameField(
            model_name="maint",
            old_name="actions",
            new_name="action",
        ),
    ]
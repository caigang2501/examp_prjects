# Generated by Django 4.2.1 on 2023-05-17 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("aw_kedro", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="submit",
            old_name="test_text",
            new_name="text",
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-18 15:34

import froala_editor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=froala_editor.fields.FroalaField(),
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-13 00:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("granja", "0003_rename_codigo_pintinho_codigo_pintinho_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pintinho",
            name="codigo_pintinho",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

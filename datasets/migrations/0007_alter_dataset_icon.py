# Generated by Django 5.0.3 on 2024-03-22 09:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("datasets", "0006_alter_dataset_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataset",
            name="icon",
            field=models.ImageField(
                null=True, upload_to="datasets/static/images/", verbose_name="Icon"
            ),
        ),
    ]
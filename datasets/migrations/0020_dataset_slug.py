# Generated by Django 4.2.11 on 2024-03-23 22:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("datasets", "0019_alter_dataset_icon"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataset",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
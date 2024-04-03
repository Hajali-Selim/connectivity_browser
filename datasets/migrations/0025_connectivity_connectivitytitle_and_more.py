# Generated by Django 4.2.11 on 2024-03-28 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("datasets", "0024_remove_functional_slug_remove_structural_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Connectivity",
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
                (
                    "sc1_matrix",
                    models.ImageField(
                        blank=True,
                        upload_to="datasets/static/images/matrices/sc1",
                        verbose_name="Relational SC matrices",
                    ),
                ),
                (
                    "sc2_matrix",
                    models.ImageField(
                        blank=True,
                        upload_to="datasets/static/images/matrices/sc2",
                        verbose_name="Layout SC matrices",
                    ),
                ),
                (
                    "sc3_matrix",
                    models.ImageField(
                        blank=True,
                        upload_to="datasets/static/images/matrices/sc3",
                        verbose_name="Pragmatic SC matrices",
                    ),
                ),
                (
                    "fc1_matrix",
                    models.ImageField(
                        blank=True,
                        upload_to="datasets/static/images/matrices/fc1",
                        verbose_name="Quantitative FC matrices",
                    ),
                ),
                (
                    "fc2_matrix",
                    models.ImageField(
                        blank=True,
                        upload_to="datasets/static/images/matrices/fc2",
                        verbose_name="Relational FC matrices",
                    ),
                ),
                (
                    "fc3_matrix",
                    models.ImageField(
                        blank=True,
                        upload_to="datasets/static/images/matrices/fc3",
                        verbose_name="Mechanistic FC matrices",
                    ),
                ),
                (
                    "fc4_matrix",
                    models.ImageField(
                        blank=True,
                        upload_to="datasets/static/images/matrices/fc4",
                        verbose_name="Propagation FC matrices",
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datasets.dataset",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ConnectivityTitle",
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
                (
                    "sc1_title",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Relational SC titles"
                    ),
                ),
                (
                    "sc2_title",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Layout SC titles"
                    ),
                ),
                (
                    "sc3_title",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        upload_to="",
                        verbose_name="Pragmatic SC titles",
                    ),
                ),
                (
                    "fc1_title",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        upload_to="",
                        verbose_name="Quantitative FC titles",
                    ),
                ),
                (
                    "fc2_title",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        upload_to="",
                        verbose_name="Relational FC titles",
                    ),
                ),
                (
                    "fc3_title",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        upload_to="",
                        verbose_name="Mechanistic FC titles",
                    ),
                ),
                (
                    "fc4_title",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        upload_to="",
                        verbose_name="Propagation FC titles",
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datasets.dataset",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="structural",
            name="dataset",
        ),
        migrations.DeleteModel(
            name="Functional",
        ),
        migrations.DeleteModel(
            name="Structural",
        ),
    ]
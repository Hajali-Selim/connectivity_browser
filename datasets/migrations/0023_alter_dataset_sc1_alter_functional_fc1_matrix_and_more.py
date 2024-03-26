# Generated by Django 4.2.11 on 2024-03-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("datasets", "0022_alter_dataset_icon_alter_functional_fc1_matrix_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataset",
            name="sc1",
            field=models.PositiveIntegerField(null=True, verbose_name="Relational SC"),
        ),
        migrations.AlterField(
            model_name="functional",
            name="fc1_matrix",
            field=models.ImageField(
                blank=True,
                upload_to="datasets/static/images/matrices/fc1",
                verbose_name="Quantitative FC matrices",
            ),
        ),
        migrations.AlterField(
            model_name="functional",
            name="fc2_matrix",
            field=models.ImageField(
                blank=True,
                upload_to="datasets/static/images/matrices/fc2",
                verbose_name="Relational FC matrices",
            ),
        ),
        migrations.AlterField(
            model_name="functional",
            name="fc3_matrix",
            field=models.ImageField(
                blank=True,
                upload_to="datasets/static/images/matrices/fc3",
                verbose_name="Mechanistic FC matrices",
            ),
        ),
        migrations.AlterField(
            model_name="functional",
            name="fc4_matrix",
            field=models.ImageField(
                blank=True,
                upload_to="datasets/static/images/matrices/fc4",
                verbose_name="Propagation FC matrices",
            ),
        ),
        migrations.AlterField(
            model_name="structural",
            name="sc1_matrix",
            field=models.ImageField(
                blank=True,
                upload_to="datasets/static/images/matrices/sc1",
                verbose_name="Relational SC matrices",
            ),
        ),
        migrations.AlterField(
            model_name="structural",
            name="sc2_matrix",
            field=models.ImageField(
                blank=True,
                upload_to="datasets/static/images/matrices/sc2",
                verbose_name="Layout SC matrices",
            ),
        ),
        migrations.AlterField(
            model_name="structural",
            name="sc3_matrix",
            field=models.ImageField(
                blank=True,
                upload_to="datasets/static/images/matrices/sc3",
                verbose_name="Pragmatic SC matrices",
            ),
        ),
    ]
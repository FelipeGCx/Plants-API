# Generated by Django 4.1.4 on 2022-12-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plants", "0003_alter_crystal_benefits_alter_crystal_chakras_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="crystal",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="plant",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]

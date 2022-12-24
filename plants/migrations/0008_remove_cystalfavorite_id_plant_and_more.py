# Generated by Django 4.1.4 on 2022-12-23 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("plants", "0007_alter_crystal_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cystalfavorite",
            name="id_plant",
        ),
        migrations.AddField(
            model_name="cystalfavorite",
            name="id_crystal",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="plants.crystalstock",
            ),
        ),
        migrations.AlterField(
            model_name="cystalfavorite",
            name="id_user",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="plants.user",
            ),
        ),
        migrations.AlterField(
            model_name="plantfavorite",
            name="id_plant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="plants.plantstock"
            ),
        ),
    ]

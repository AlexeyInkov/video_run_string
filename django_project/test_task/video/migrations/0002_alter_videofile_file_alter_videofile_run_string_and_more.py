# Generated by Django 4.2 on 2024-03-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("video", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="videofile",
            name="file",
            field=models.FileField(null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="videofile",
            name="run_string",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="videofile",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
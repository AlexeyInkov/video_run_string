# Generated by Django 4.2 on 2024-03-26 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VideoFile",
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
                ("run_string", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
                ("file", models.FileField(upload_to="")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

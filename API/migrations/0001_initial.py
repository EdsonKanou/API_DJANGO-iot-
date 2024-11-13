# Generated by Django 5.0.3 on 2024-04-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="sensor",
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
                ("nom", models.CharField(blank=True, max_length=20)),
                ("postion", models.CharField(blank=True, max_length=70)),
                ("state", models.IntegerField(blank=True)),
                ("status", models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]

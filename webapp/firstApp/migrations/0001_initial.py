# Generated by Django 5.1.6 on 2025-02-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="aids",
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
                ("age", models.IntegerField()),
                ("sex", models.IntegerField()),
                ("bmi", models.IntegerField()),
                ("children", models.IntegerField()),
                ("smoker", models.IntegerField()),
                ("region", models.IntegerField()),
            ],
        ),
    ]

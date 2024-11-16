# Generated by Django 4.2 on 2024-11-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RegularHabit",
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
                ("place", models.CharField(max_length=200, verbose_name="место")),
                ("action", models.TextField(verbose_name="действие")),
                ("start_time", models.DateTimeField(verbose_name="время начала")),
                ("end_time", models.DateTimeField(verbose_name="время окончания")),
                ("public", models.BooleanField(verbose_name="публичность")),
                ("award", models.TextField(verbose_name="вознаграждение")),
                (
                    "frequency",
                    models.CharField(
                        choices=[("ежедневно", "Daily"), ("еженедельно", "Weekly")],
                        default="ежедневно",
                        max_length=12,
                        verbose_name="периодичность",
                    ),
                ),
                (
                    "is_enjoyable",
                    models.BooleanField(verbose_name="признак приятности"),
                ),
            ],
            options={
                "verbose_name": "обычная привычка",
                "verbose_name_plural": "обычные привычки",
            },
        ),
        migrations.CreateModel(
            name="RelatedHabit",
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
                ("place", models.CharField(max_length=200, verbose_name="место")),
                ("action", models.TextField(verbose_name="действие")),
                ("start_time", models.DateTimeField(verbose_name="время начала")),
                ("end_time", models.DateTimeField(verbose_name="время окончания")),
                ("public", models.BooleanField(verbose_name="публичность")),
                ("award", models.TextField(verbose_name="вознаграждение")),
            ],
            options={
                "verbose_name": "желаемая привычка",
                "verbose_name_plural": "желаемые привычки",
            },
        ),
    ]

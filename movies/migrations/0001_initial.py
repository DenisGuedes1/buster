# Generated by Django 4.2 on 2023-04-13 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("G", "G"),
                            ("PG", "Pg"),
                            ("PG-13", "Pg 13"),
                            ("R", "R"),
                            ("NC-17", "Nc 17"),
                        ],
                        default="G",
                        max_length=10,
                    ),
                ),
                ("synopsis", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderMovie",
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
                ("buyed_at", models.DateTimeField(auto_now_add=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "movies",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_movies",
                        to="movies.movie",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_movies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

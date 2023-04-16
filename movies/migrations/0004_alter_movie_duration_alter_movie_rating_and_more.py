# Generated by Django 4.2 on 2023-04-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0003_ordermovie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="rating",
            field=models.CharField(
                choices=[
                    ("G", "G"),
                    ("PG", "Pg"),
                    ("PG-13", "Pg 13"),
                    ("R", "R"),
                    ("NC-17", "Nc 17"),
                ],
                default="G",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="synopsis",
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
# Generated by Django 4.2 on 2023-04-16 19:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0004_alter_movie_duration_alter_movie_rating_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="OrderMovie",
            new_name="MovieOrder",
        ),
    ]

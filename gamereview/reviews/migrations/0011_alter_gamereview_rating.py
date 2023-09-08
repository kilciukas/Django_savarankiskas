# Generated by Django 4.2.4 on 2023-09-08 17:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_gamereview_rating_alter_game_cover_alter_game_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamereview',
            name='rating',
            field=models.PositiveIntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Rating'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-20 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='stars',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='stars',
            name='person_id',
        ),
        migrations.DeleteModel(
            name='Directors',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
        migrations.DeleteModel(
            name='People',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
        migrations.DeleteModel(
            name='Stars',
        ),
    ]
# Generated by Django 4.1 on 2022-11-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_comicbook_author_comicbook_authors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comicbook',
            name='illustrator',
        ),
        migrations.AddField(
            model_name='comicbook',
            name='illustrators',
            field=models.ManyToManyField(to='api.illustrator'),
        ),
        migrations.RemoveField(
            model_name='comicbook',
            name='characters',
        ),
        migrations.AddField(
            model_name='comicbook',
            name='characters',
            field=models.ManyToManyField(to='api.character'),
        ),
    ]
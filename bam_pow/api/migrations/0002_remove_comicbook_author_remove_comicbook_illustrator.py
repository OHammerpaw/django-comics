# Generated by Django 4.1 on 2022-11-22 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comicbook',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comicbook',
            name='illustrator',
        ),
    ]
# Generated by Django 4.1 on 2022-11-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_comicbook_cover_alter_comicbook_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='alias',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='details',
            field=models.CharField(max_length=1000),
        ),
    ]
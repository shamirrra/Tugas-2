# Generated by Django 4.1 on 2022-11-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_alter_watchlist_watched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='watched',
            field=models.BooleanField(),
        ),
    ]

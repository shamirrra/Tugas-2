# Generated by Django 4.1.2 on 2022-12-29 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0003_alter_watchlist_watched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='watched',
            field=models.TextField(),
        ),
    ]

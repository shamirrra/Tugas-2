# Generated by Django 4.1 on 2022-09-22 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='watched',
            field=models.TextField(),
        ),
    ]
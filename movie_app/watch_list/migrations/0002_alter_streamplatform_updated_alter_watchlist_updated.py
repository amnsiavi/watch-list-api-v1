# Generated by Django 5.0.6 on 2024-05-30 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamplatform',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
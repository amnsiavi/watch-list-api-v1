# Generated by Django 5.0.6 on 2024-05-30 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_list', '0003_watchlist_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch', to='watch_list.streamplatform'),
        ),
    ]

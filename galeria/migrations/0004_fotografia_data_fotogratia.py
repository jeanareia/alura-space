# Generated by Django 5.1.3 on 2024-11-12 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_fotogratia',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

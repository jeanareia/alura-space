# Generated by Django 5.1.3 on 2024-11-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_data_fotogratia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/'),
        ),
    ]

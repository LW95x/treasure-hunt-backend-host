# Generated by Django 5.0.1 on 2024-01-08 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treasure_hunt_backend', '0004_rename_latitude_treasure_lat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treasure',
            old_name='lat',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='treasure',
            old_name='lng',
            new_name='longitude',
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-08 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treasure_hunt_backend', '0003_rename_user_profile_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treasure',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='treasure',
            old_name='longitude',
            new_name='lng',
        ),
    ]

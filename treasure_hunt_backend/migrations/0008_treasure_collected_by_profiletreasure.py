# Generated by Django 5.0.1 on 2024-01-09 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure_hunt_backend', '0007_remove_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='collected_by',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ProfileTreasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treasure_hunt_backend.profile')),
                ('treasure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treasure_hunt_backend.treasure')),
            ],
        ),
    ]
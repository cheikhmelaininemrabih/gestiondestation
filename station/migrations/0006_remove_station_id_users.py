# Generated by Django 4.2.7 on 2023-11-16 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0005_alter_station_id_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='id_users',
        ),
    ]

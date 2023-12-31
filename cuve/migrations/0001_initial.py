# Generated by Django 4.2.6 on 2023-11-01 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuve',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nb_pmp_alimente', models.IntegerField()),
                ('charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stocke', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Qt_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='station.station')),
            ],
        ),
    ]

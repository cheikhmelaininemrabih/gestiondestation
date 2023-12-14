# Generated by Django 4.2.7 on 2023-11-15 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuve', '0003_cuve_is_active'),
        ('station', '0003_station_is_active'),
        ('pompe', '0003_alter_pompe_id_pompiste'),
        ('pompiste', '0002_pompiste_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='pompiste',
            name='cuve',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cuve.cuve'),
        ),
        migrations.AddField(
            model_name='pompiste',
            name='pompe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pompe.pompe'),
        ),
        migrations.AddField(
            model_name='pompiste',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pompistes_by_station', to='station.station'),
        ),
        migrations.AlterField(
            model_name='pompiste',
            name='id_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pompistes_by_id', to='station.station'),
        ),
    ]
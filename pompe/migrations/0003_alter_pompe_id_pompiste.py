# Generated by Django 4.2.7 on 2023-11-15 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pompiste', '0002_pompiste_is_active'),
        ('pompe', '0002_pompe_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pompe',
            name='id_pompiste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pompes', to='pompiste.pompiste'),
        ),
    ]
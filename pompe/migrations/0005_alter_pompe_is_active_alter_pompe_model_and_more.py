# Generated by Django 4.2.6 on 2023-12-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pompe', '0004_alter_pompe_id_pompiste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pompe',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='pompe',
            name='model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pompe',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

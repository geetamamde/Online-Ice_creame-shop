# Generated by Django 4.2 on 2023-12-30 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordermaster',
            options={},
        ),
        migrations.AddField(
            model_name='mycart',
            name='ice_creame',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.ice_creame'),
        ),
        migrations.AlterModelTable(
            name='mycart',
            table='mycart',
        ),
    ]
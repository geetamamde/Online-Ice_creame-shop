# Generated by Django 4.2 on 2024-01-01 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_cheesecake_rename_price_coldcoffee_cold_price'),
        ('frontend', '0002_alter_ordermaster_options_mycart_ice_creame_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycart',
            name='cheese_cake',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.cheesecake'),
        ),
        migrations.AddField(
            model_name='mycart',
            name='cold_coffee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.coldcoffee'),
        ),
    ]

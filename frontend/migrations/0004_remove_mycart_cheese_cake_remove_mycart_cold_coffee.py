# Generated by Django 4.2 on 2024-01-01 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_mycart_cheese_cake_mycart_cold_coffee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycart',
            name='cheese_cake',
        ),
        migrations.RemoveField(
            model_name='mycart',
            name='cold_coffee',
        ),
    ]

# Generated by Django 4.2 on 2024-01-03 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_contact_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_info',
            old_name='f_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='contact_info',
            old_name='l_name',
            new_name='lastname',
        ),
    ]
# Generated by Django 3.2 on 2022-07-06 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_service_icons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-13 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210413_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='user',
        ),
    ]

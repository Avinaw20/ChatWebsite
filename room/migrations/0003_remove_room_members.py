# Generated by Django 4.0.6 on 2022-08-10 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_room_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='members',
        ),
    ]

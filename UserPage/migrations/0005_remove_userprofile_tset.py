# Generated by Django 4.2.7 on 2023-12-05 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserPage', '0004_userprofile_tset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='tset',
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-06 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Completed',
        ),
        migrations.DeleteModel(
            name='Games',
        ),
    ]
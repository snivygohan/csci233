# Generated by Django 4.2.7 on 2023-12-05 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.TextField(default='', max_length=245),
        ),
    ]
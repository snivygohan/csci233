# Generated by Django 5.0 on 2023-12-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserPage', '0005_remove_userprofile_tset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/profile/default.png', null=True, upload_to='profile/'),
        ),
    ]

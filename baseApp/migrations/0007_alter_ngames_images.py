# Generated by Django 4.2.7 on 2023-11-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0006_ngames'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngames',
            name='images',
            field=models.TextField(),
        ),
    ]

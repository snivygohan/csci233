# Generated by Django 4.2.7 on 2023-11-27 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='collections',
            name='status',
            field=models.CharField(blank=True, choices=[('Playing', 'Playing'), ('Completed', 'Completed'), ('Dropped', 'Dropped')], max_length=10, null=True),
        ),
    ]

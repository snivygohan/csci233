# Generated by Django 5.0 on 2023-12-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0005_unaccent'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
            ],
            options={
                'db_table': 'game_requests',
                'managed': True,
            },
        ),
    ]

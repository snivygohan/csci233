# Generated by Django 4.2.6 on 2023-11-01 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.games')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.authuser')),
            ],
            options={
                'db_table': 'collections',
                'managed': True,
            },
        ),
    ]
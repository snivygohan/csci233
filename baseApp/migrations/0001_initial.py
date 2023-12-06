# Generated by Django 4.2.7 on 2023-11-11 21:13

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.contrib.postgres.fields

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('release_date', models.CharField(max_length=255)),
                ('team', models.CharField(max_length=255)),
                ('esrb', models.CharField(choices=[('E', 'E'), ('E10+', 'E10'), ('T', 'T'), ('M', 'M'), ('NR', 'Norating')], default='NR', max_length=255)),
                ('platforms', models.CharField(max_length=255)),
                ('multiplayer', models.BooleanField()),
                ('genres', models.CharField(max_length=255)),
                ('images', models.CharField(max_length=255)),
                ('summary', models.TextField()),
            ],
            options={
                'db_table': 'games',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('Playing', 'Playing'), ('Completed', 'Completed'), ('Dropped', 'Dropped')], max_length=10)),
                ('favorite', models.BooleanField(default=False)),
                ('currentUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('games', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='baseApp.games')),
            ],
            options={
                'verbose_name_plural': 'Collections',
                'db_table': 'collections',
                'managed': True,
            },
        ),
    ]

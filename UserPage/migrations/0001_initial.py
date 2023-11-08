# Generated by Django 4.2.7 on 2023-11-07 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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

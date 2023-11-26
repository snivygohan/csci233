from django.contrib.postgres.operations import UnaccentExtension

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0012_alter_games_genres_alter_games_team'),
    ]

    operations = [
        UnaccentExtension(),
    ]
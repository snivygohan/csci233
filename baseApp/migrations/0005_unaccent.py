from django.contrib.postgres.operations import UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0004_auto_20231126_2159'),
    ]

    operations = [
        UnaccentExtension()
    ]
from django.db import models

# Create your models here.

# still learning the ORM part of django, so i put my code here in comment(s) -kev
#class LoginInfo(models.Model):
#    username = models.CharField(max_Length=25)
#    email = models.CharField(max_Length=100)
#    password1 = models.CharField(max_Length=50)

#going to need to confer with steve to see how to hook up this model to admin and then our postgres db later. -kev
class Games(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.CharField(db_column='Release Date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    team = models.CharField(max_length=255, blank=True, null=True)
    esrb = models.CharField(max_length=255, blank=True, null=True)
    platforms = models.CharField(max_length=255, blank=True, null=True)
    multiplayer = models.BooleanField(blank=True, null=True)
    genres = models.CharField(max_length=255, blank=True, null=True)
    images = models.CharField(max_length=255, blank=True, null=True)
    summary = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'
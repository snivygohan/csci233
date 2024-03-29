from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings

# Create your models here.

class Games(models.Model):
    class ESRB_Rating(models.TextChoices):
        E = 'E'
        E10 = 'E10+'
        T = 'T'
        M = 'M'
        NORATING = 'NR'

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    release_date = models.DateField(max_length=255)
    team = models.CharField(max_length=255)
    esrb = models.CharField(max_length=255, choices=ESRB_Rating.choices, default=ESRB_Rating.NORATING)
    platforms = models.CharField(max_length=255)
    multiplayer = models.BooleanField()
    genres = models.CharField(max_length=255)
    images = models.TextField()
    summary = models.TextField()

    def __str__(self):
        return str(self.title)
    
    class Meta:
        managed = True
        db_table = 'games'

class Collections(models.Model):
    class GameStatus(models.TextChoices):
        PLAYING = 'Playing'
        COMPLETED = 'Completed'
        Dropped = 'Dropped'

    currentUser = models.ForeignKey(settings.AUTH_USER_MODEL, related_name= 'owner', null = True, on_delete= models.SET_NULL)  
    games = models.ForeignKey(Games, related_name='games', null = True, on_delete= models.SET_NULL)
    status = models.CharField(max_length=10, blank= True, null = True, choices=GameStatus.choices)
    favorite = models.BooleanField(default= False)

    def __str__(self):
        return f'({self.currentUser}-{self.games})'
    
    class Meta:
        managed = True
        db_table = 'collections'
        verbose_name_plural = 'Collections'

class GameRequests(models.Model):
    
    title = models.TextField(null = True)

    class Meta:
        managed = True
        db_table = 'game_requests'
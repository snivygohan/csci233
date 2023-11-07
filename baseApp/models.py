from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Games(models.Model):

    ESRB = (
        ('E', 'E'),
        ('E10+', 'E10+'),
        ('T', 'T'),
        ('M', 'M'),
        ('NR', 'NR')
    )
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    release_date = models.CharField(db_column='Release Date', max_length=255)
    team = models.CharField(max_length=255)
    esrb = models.CharField(max_length=255, choices=ESRB)
    platforms = models.CharField(max_length=255)
    multiplayer = models.BooleanField()
    genres = models.CharField(max_length=255)
    images = models.CharField(max_length=255)
    summary = models.TextField()

    def __str__(self):
        return str(self.title)
    
    class Meta:
        managed = False
        db_table = 'games'

class Collections(models.Model):
    currentUser = models.ForeignKey(User, related_name= 'owner', null = True, on_delete= models.SET_NULL)  
    games = models.ForeignKey(Games, related_name='games', null = True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.currentUser.__str__()
    
    class Meta:
        managed = True
        db_table = 'collections'
        verbose_name_plural = 'Collections'

    @classmethod
    def addGame(cls, currentUser, newGame):
        collection, created = cls.objects.get_or_create( currentUser = currentUser )
        collection.games.add(newGame)

    @classmethod
    def removeGame(cls, currentUser, newGame):
        collection, created = cls.objects.get_or_create( currentUser = currentUser )
        collection.games.remove(newGame)

class Completed(models.Model):
    user_id = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    game_ids = models.ForeignKey(Games, models.DO_NOTHING, db_column='game_ids', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'completed'
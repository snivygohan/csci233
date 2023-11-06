from django.db import models
from baseApp.models import *
from login.models import *

# Create your models here.
class Collections(models.Model):
    currentUser = models.ForeignKey(AuthUser, related_name= 'owner', null = True, on_delete= models.SET_NULL)  
    games = models.ManyToManyField(Games)
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



        

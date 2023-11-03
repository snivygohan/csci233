# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django .shortcuts import reverse 

# Create your models here.


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    def __str__(self):
        return str(self.username)
    class Meta:
        managed = False
        db_table = 'auth_user'



class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Completed(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    game_ids = models.ForeignKey('Games', models.DO_NOTHING, db_column='game_ids', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'completed'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Games(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    release_date = models.CharField(db_column='Release Date', max_length=255)
    team = models.CharField(max_length=255)
    esrb = models.CharField(max_length=255)
    platforms = models.CharField(max_length=255)
    multiplayer = models.BooleanField()
    genres = models.CharField(max_length=255)
    images = models.CharField(max_length=255)
    summary = models.TextField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("/game", args={str(self.id)})
    
    class Meta:
        managed = False
        db_table = 'games'
        verbose_name_plural = 'Games'
    
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
        
        
        



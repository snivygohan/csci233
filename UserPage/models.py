from django.db import models
from baseApp.models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null = True) 
    about = models.TextField(max_length = 255, default = '')
    profile_pic = models.ImageField(null = True, blank = True, upload_to = "profile/", default = '/profile/default.png')
    
    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])
            
    post_save.connect(create_profile, sender = User)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        managed = True
        db_table = 'UserPage_userprofile'
    
    



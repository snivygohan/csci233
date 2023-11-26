<<<<<<< HEAD
from django.shortcuts import get_object_or_404, render
from baseApp.models import Games, Collections
from UserPage.models import UserProfile
from login.models import *
from django.contrib.auth.models import User

# Create your views here.
def profile(request,pk):
    userpk = UserProfile.objects.get(user_id = pk)
    userCollection = Collections.objects.filter(currentUser__exact = pk)
    args = {'user':request.user, 'test':userCollection, 'pageuser':userpk}
    return render(request,'profile.html',args)
=======
from django.shortcuts import render
from baseApp.models import Games 

# Create your views here.

def profile(request):
   args = {'user': request.user}
   return render(request, 'profile.html')
    
>>>>>>> testSteve

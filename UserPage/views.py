from django.shortcuts import get_object_or_404, render, redirect
from baseApp.models import Games, Collections
from UserPage.models import UserProfile
from login.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def profile(request,pk):
    pageUser = UserProfile.objects.get(user_id = pk)
    currentUser = request.user.id
    userCollection = Collections.objects.filter(currentUser__exact = pk)
    Favorite = Collections.objects.filter(currentUser__exact = pk, favorite = True)
    currentlyPlaying = Collections.objects.filter(currentUser__exact = pk, status = Collections.GameStatus.PLAYING)
    finished = Collections.objects.filter(currentUser__exact = pk, status = Collections.GameStatus.COMPLETED)
    context = {}

    # Define template variables 
    is_self = False
    is_friend = False
    
    if currentUser == pageUser.user_id:
        is_self = True
    elif currentUser != pageUser.user.id:
        is_self = False
    
   


    context['user'] = request.user
    context['collection'] = userCollection
    context['pageuser'] = pageUser
    context['currentUser'] = currentUser
    context['is_self'] = is_self
    context['Favorite'] = Favorite 
    context['currentlyPlaying'] = currentlyPlaying
    context['finished'] = finished




    return render(request,'profile.html',context)



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
    currentUser = UserProfile.objects.get(user_id = request.user.id)
    userCollection = Collections.objects.filter(currentUser__exact = pk)
    Favorite = Collections.objects.filter(currentUser__exact = pk, favorite = True)
    currentlyPlaying = Collections.objects.filter(currentUser__exact = pk, status = Collections.GameStatus.PLAYING)
    finished = Collections.objects.filter(currentUser__exact = pk, status = Collections.GameStatus.COMPLETED)
    context = {}

    # Define template variables 
    is_self = False
    is_friend = False
    
    if currentUser.user_id == pageUser.user_id:
        is_self = True
    elif currentUser.user_id != pageUser.user.id:
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


def account_search_view(request, *args, **kwargs):
    context = {}
    if request.method == "GET":
        search_query = request.GET.get("q")
        if len(search_query) > 0:
            search_result = UserProfile.objects.filter(user__icontains = search_query).distinct()
            user = request.user
            profiles = []
            for profiles in search_result:
                profiles.append((profile,False))
    return render(request, "search_results.html", context)
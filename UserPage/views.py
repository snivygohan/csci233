from django.shortcuts import get_object_or_404, render, redirect
from baseApp.models import Games, Collections
from UserPage.models import UserProfile
from login.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings
from .forms import AccountUpdateForm

# Create your views here.
def profile(request,pk):
    pageUser = UserProfile.objects.get(user_id = pk)
    currentUser = request.user.id
	
    userCollection = Collections.objects.filter(currentUser__exact = pk)
    collectionDisplay = Collections.objects.filter(currentUser__exact = pk)[:7]
	
    Favorite = Collections.objects.filter(currentUser__exact = pk, favorite = True)
    faveDisplay = Collections.objects.filter(currentUser__exact = pk, favorite = True)[:7]
	
    currentlyPlaying = Collections.objects.filter(currentUser__exact = pk, status = Collections.GameStatus.PLAYING)
    currentDisplay = Collections.objects.filter(currentUser__exact = pk, status = Collections.GameStatus.PLAYING) [:7]
	
    finished = Collections.objects.filter(currentUser__exact = pk, status = Collections.GameStatus.COMPLETED)
    finishedDisplay = Collections.objects.filter(currentUser__exact = pk, status = Collections.GameStatus.COMPLETED)[:7]
	
    numCollection = Collections.objects.filter(currentUser__exact = pk).count()
    numCompleted = Collections.objects.filter(currentUser__exact = pk, status = Collections.GameStatus.COMPLETED).count()
	
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
    context['numCollection'] = numCollection
    context['numCompleted'] = numCompleted
    context['faveDisplay'] = faveDisplay
    context['collectionDisplay'] = collectionDisplay
    context['currentDisplay'] = currentDisplay
    context['finishedDisplay'] = finishedDisplay

    return render(request,'profile.html',context)


def edit_account_view(request,pk):
	if not request.user.is_authenticated:
		return redirect("login")
	submitted = False
	user_id = request.user.id
	account = UserProfile.objects.get(user_id = pk)
	context = {}
	if request.method == 'POST':
		form = AccountUpdateForm(request.POST,request.FILES or None, instance = account)

		if form.is_valid():
			form.save()
			return redirect("profile", pk)
		else:
			form = AccountUpdateForm()
			if 'submitted' in request.GET:
				submitted = True
	form = AccountUpdateForm()        
	context = {'form':form, 'submitted':submitted}
	return render(request, 'edit_account.html', context)


def fullCollection(request,pk):
    pageUser = UserProfile.objects.get(user_id = pk)
    currentUser = request.user.id
    userCollection = Collections.objects.filter(currentUser__exact = pk)
    context = {}
	
    context['user'] = request.user
    context['collection'] = userCollection
    context['pageuser'] = pageUser
    context['currentUser'] = currentUser
	
	
    return render(request, 'collection.html', context)

def favorites(request,pk):
    pageUser = UserProfile.objects.get(user_id = pk)
    currentUser = request.user.id
    favorite = Collections.objects.filter(currentUser__exact = pk, favorite = True)
    context = {}
	
    context['user'] = request.user
    context['favorite'] = favorite
    context['pageuser'] = pageUser
    context['currentUser'] = currentUser
	
	
    return render(request, 'favorite.html', context)

def current(request,pk):
    pageUser = UserProfile.objects.get(user_id = pk)
    currentUser = request.user.id
    currentlyPlaying = Collections.objects.filter(currentUser__exact = pk, status = Collections.GameStatus.PLAYING)
    context = {}
	
    context['user'] = request.user
    context['currentlyPlaying'] = currentlyPlaying
    context['pageuser'] = pageUser
    context['currentUser'] = currentUser
	
	
    return render(request, 'currentlyPlaying.html', context)

def finished(request,pk):
    pageUser = UserProfile.objects.get(user_id = pk)
    currentUser = request.user.id
    finished = Collections.objects.filter(currentUser__exact = pk, status = Collections.GameStatus.COMPLETED)
    context = {}
	
    context['user'] = request.user
    context['finished'] = finished
    context['pageuser'] = pageUser
    context['currentUser'] = currentUser
	
	
    return render(request, 'finished.html', context)
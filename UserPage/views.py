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




"""def account_view(request, *args, **kwargs):

	Tutorials version that doesnt seem to work 
def account_view(request, *args, **kwargs):
	- Logic here is kind of tricky
		is_self (boolean)
			is_friend (boolean)
				-1: NO_REQUEST_SENT
				0: THEM_SENT_TO_YOU
				1: YOU_SENT_TO_THEM
	
	
	context = {}
	user_id = kwargs.get("user_id")
	try:
		account = UserProfile.objects.get(pk= user_id)
	except:
		return HttpResponse("Something went wrong.")
	if account:
		context['id'] = account
		context['user'] = account.user
		context['profile_pic'] = account.profile_pic.url

		# Define template variables
		test = "hello"
		is_self = True
		is_friend = False
		user = request.user.id
		#if user.is_authenticated and is_test is True:
		#	is_self = True
		#elif not user.is_authenticated:
		#	is_self = False
			
		# Set the template variables to the values
		context['hello'] = test
		context['is_self'] = is_self
		context['is_friend'] = is_friend
		context['BASE_URL'] = settings.BASE_URL
		return render(request, "profile.html", context)
"""
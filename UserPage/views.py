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


def edit_account_view(request,pk):
	if not request.user.is_authenticated:
		return redirect("login")
	user_id = request.user.id
	account = UserProfile.objects.get(user_id = pk)
	context = {}
	if request.POST:
		form = UserProfile(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			new_username = form.cleaned_data['username']
			return redirect("account:view", user_id=account.pk)
		else:
			form = UserProfile(request.POST, instance=request.user,
				initial={
					"id": account.pk,
					"email": account.email, 
					"username": account.user,
					"profile_image": account.profile_pic,
					"hide_email": account.hide_email,
					"about":account.about,
				}
			)
			context['form'] = form
	else:
		form = UserProfile(
			initial={
					"id": account.pk,
					"email": account.email, 
					"username": account.user,
					"profile_image": account.profile_pic,
					"hide_email": account.hide_email,
					"about":account.about,
				}
			)
		context['form'] = form
	context['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
	return render(request, "account/edit_account.html", context)

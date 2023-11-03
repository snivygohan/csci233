from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

# Create your views here.
from .forms import *
from .models import *



@login_required(login_url='login')
def home_page(request):
    gimages = Games.objects.only('images')[:5]
    context = {'gimages':gimages}
    return render(request, 'base.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        return render(request, 'login.html')
    
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('login')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Registration Successful')
                return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)

def profile(request):
   args = {'user': request.user}
   return render(request, 'accounts/user.html')
    

class gameView(ListView):
    model = Games
    template_name = "gamesList.html"

class gameDetailView(DetailView):
    model = Games
    template_name = "game.html"

def add_game(request):
    submitted = False
    if request.method == 'POST':
        form = AddGameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addgame?submitted=True')
    else:
        form = AddGameForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {'form':form, 'submitted':submitted}
    return render(request, 'addgame.html', context)


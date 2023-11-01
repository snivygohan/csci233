from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Games

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddGameForm(ModelForm):
    class Meta:
        model = Games
        fields = ['title', 'release_date', 'team', 'esrb', 'platforms', 'multiplayer', 'genres', 'images', 'summary']


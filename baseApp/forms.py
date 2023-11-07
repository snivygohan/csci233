from django.forms import ModelForm
from django import forms
from .models import Games

class AddGameForm(ModelForm):
    class Meta:
        model = Games
        fields = ['title', 'release_date', 'team', 'esrb', 'platforms', 'multiplayer', 'genres', 'images', 'summary']
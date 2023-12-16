from django.forms import ModelForm
from django import forms
from .models import GameRequests

class AddGameForm(ModelForm):
    class Meta:
        model = GameRequests
        fields = ['title']
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from UserPage.models import UserProfile

class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('about', 'profile_pic')
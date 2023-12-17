from django.forms import ModelForm
from django import forms
from .models import Collections

class UpdateCollection(forms.ModelForm):
    class Meta:
        model = Collections
        fields = ['games']

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from models import UserProfile

class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'about','email', 'profile_image', 'hide_email' )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = UserProfile.objects.exclude(pk=self.instance.pk).get(email=email)
        except UserProfile.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_about(self):
        about = self.cleaned_data['about']
        try:
            account = UserProfile.objects.exclude(pk=self.instance.pk).get(about=about)
        except UserProfile.DoesNotExist:
            return about
        raise forms.ValidationError('About "%s" is already in use.' % about)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = UserProfile.objects.exclude(pk=self.instance.pk).get(username=username)
        except UserProfile.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)
    



    def save(self, commit=True):
        account = super(AccountUpdateForm, self).save(commit=False)
        account.username = self.cleaned_data['username']
        account.email = self.cleaned_data['email'].lower()
        account.profile_image = self.cleaned_data['profile_image']
        account.hide_email = self.cleaned_data['hide_email']
        account.about = self.cleaned_data['about']
        if commit:
            account.save()
        return account
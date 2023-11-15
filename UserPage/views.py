from typing import Any
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from baseApp.models import Games, Collections
from UserPage.models import UserProfile
from login.models import *
from django.contrib.auth.models import User

# Create your views here.

class ShowProfilePageView(DetailView):
   model = UserProfile
   template_name = 'profile.html'

   def get_context_data(self, *args, **kwargs):
      users =   UserProfile.objects.all()
      context = super(ShowProfilePageView, self).get_context_data(self, *args, **kwargs)
      page_user = get_object_or_404(UserProfile, id = self.kwargs['pk'])
      context = ["page_user"]
      return context




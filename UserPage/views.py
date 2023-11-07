from django.shortcuts import render
from baseApp.models import Games 

# Create your views here.

def profile(request):
   args = {'user': request.user}
   return render(request, 'profile.html')
    

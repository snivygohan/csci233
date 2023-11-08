from django.shortcuts import render
from django.http import HttpResponse
from .models import Games

# Create your views here.

def games_page(request):
    return render(request, 'games.html')

def all_games(request):
    games_list = Games.objects.all()[:10]
    return render(request, 'allGames.html', {'games_list':games_list})

def game_detail_view(request, id=None):
    gameDetails=None
    if id is not None:
        gameDetails = Games.objects.get(id=id)
    #game = Games.objects.all()
    context = {"object":gameDetails,}
    return render(request, 'games.html', context)

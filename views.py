from django.shortcuts import render
from django.http import HttpResponse
from .models import Games
from django.core.paginator import Paginator

# Create your views here.

def games_page(request):
    return render(request, 'games.html')

def all_games(request):
    p = Paginator(Games.objects.all(), 48)
    page = request.GET.get('page')
    games = p.get_page(page)
    return render(request, 'allGames.html', {'games':games})

def game_detail_view(request, id=None):
    gameDetails=None
    if id is not None:
        gameDetails = Games.objects.get(id=id)
    context = {"object":gameDetails,}
    return render(request, 'games.html', context)

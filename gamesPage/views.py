from django.shortcuts import render
from django.http import HttpResponse
from .models import Games

# Create your views here.

def games_page(request):
    return render(request, 'games.html')

def all_games(request):
    games_list = Games.objects.all()[:10]
    return render(request, 'allGames.html', {'games_list':games_list})

def game(request, id):
    id = Games.objects.get(id=id)
    game = Games.objects.all()
    context = {'id':id}, {'game':game}
    return render(request, 'games.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Games, Collections
# Create your views here.


def all_games(request):
    games_list = Games.objects.all()[:10]
    return render(request, 'allGames.html', {'games_list':games_list})

def game_page(request, id):
        
    gameDetails = Games.objects.get(id=id)

    if id is not None and request.user.is_authenticated:
    
        verifyCollection = Collections.objects.filter(currentUser = request.user, games_id = id).exists()
        verifyFavorite = Collections.objects.filter(currentUser = request.user, games_id = id, favorite = True).exists()
        verifyStatus = Collections.objects.filter(currentUser = request.user, games_id = id, status__isnull=False).exists()

        if verifyStatus == True:
            getStatus = Collections.objects.get(currentUser = request.user, games_id = id, status__isnull=False)

            context = {"object":gameDetails, "verifyc":verifyCollection, "verifyf":verifyFavorite, "verifys":verifyStatus, "gstatus":getStatus}
            return render(request, 'games.html', context)
        else:
            context = {"object":gameDetails, "verifyc":verifyCollection, "verifyf":verifyFavorite, "verifys":verifyStatus}
            return render(request, 'games.html', context)
        
    else:
        context = {"object":gameDetails}
        return render(request, 'games.html', context)

def add_game(request):
    
    if request.method == "POST":
        id = request.POST['addcollection']
        Collections.objects.get_or_create(currentUser = request.user, games_id = id)

    return redirect('game', id)

def remove_game(request):
     
    if request.method == "POST":
        id = request.POST['delcollection']
        Collections.objects.filter(currentUser = request.user, games_id = id).delete()

    return redirect('game', id)

def favorite_game(request, id):

    collection = Collections.objects.get(currentUser = request.user, games_id = id)

    if request.method == "POST":
        value = request.POST['favorite']
        collection.favorite = value
        collection.save()

    return redirect('game', id)

def status_game(request, id):

    collection = Collections.objects.get(currentUser = request.user, games_id = id)

    if request.method == "POST":
        value = request.POST['status']
        collection.status = value
        collection.save()

    return redirect('game', id)
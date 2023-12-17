from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Games, Collections, UserProfile
from django.core.paginator import Paginator
from .filters import GenreFilter
from .forms import UpdateCollection



def all_games(request):

    genre_filter = GenreFilter(request.GET, queryset=Games.objects.all())
    searched = ''
    results = genre_filter.qs

    if request.method == 'GET' and 'searched' in request.GET:
        searched = request.GET['searched']
        if searched is not None and searched != '':
            results = genre_filter.qs.filter(title__unaccent__icontains=searched)

    p = Paginator(results, 48)
    page = request.GET.get('page')
    games = p.get_page(page)

    context = {'games':games, 'form':genre_filter.form, 'search':searched}
    return render(request, 'allGames.html', context)

def game_page(request, id):
        
    gameDetails = Games.objects.get(id=id)
    playingUsers = Collections.objects.filter(games_id = id, status = "Playing")[:10]

    if id is not None and request.user.is_authenticated:
    
        verifyCollection = Collections.objects.filter(currentUser = request.user, games_id = id).exists()
        verifyFavorite = Collections.objects.filter(currentUser = request.user, games_id = id, favorite = True).exists()
        verifyStatus = Collections.objects.filter(currentUser = request.user, games_id = id, status__isnull=False).exists()

        if verifyStatus == True:
            getStatus = Collections.objects.get(currentUser = request.user, games_id = id, status__isnull=False)

            context = {"object":gameDetails, "verifyc":verifyCollection, 
                       "verifyf":verifyFavorite, "verifys":verifyStatus, 
                       "gstatus":getStatus, "playing":playingUsers}
            return render(request, 'games.html', context)
        else:
            context = {"object":gameDetails, "verifyc":verifyCollection, 
                       "verifyf":verifyFavorite, "verifys":verifyStatus,
                       "playing":playingUsers}
            return render(request, 'games.html', context)
        
    else:
        context = {"object":gameDetails, "playing":playingUsers}
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
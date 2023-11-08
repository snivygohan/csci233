from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Games
from .forms import AddGameForm
from .filters import GenreFilter
# Create your views here.


@login_required(login_url='login')
def home_page(request):
    gimages = Games.objects.order_by('?')[:12]

    context = {'gimages':gimages}
    return render(request, 'base.html', context)

def filter_test(request):
    genre_filter = GenreFilter(request.GET, queryset=Games.objects.all())

    context = {'form':genre_filter.form, 
               'games':genre_filter.qs}
    return render(request, 'testpage.html', context)

def search_game(request):
    if 'searched' in request.GET:
        searched = request.GET['searched']
        results = Games.objects.filter(title__icontains=searched) 
        return render(request, 'search.html', {'searched':searched, 'results':results})
    else:
        return render(request, 'search.html')
    
@login_required(login_url='login')
def add_game(request):
    submitted = False
    if request.method == 'POST':
        form = AddGameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addgame?submitted=True')
    else:
        form = AddGameForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {'form':form, 'submitted':submitted}
    return render(request, 'addgame.html', context)
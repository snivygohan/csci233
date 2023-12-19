from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Games, Collections
from .forms import AddGameForm
#from .filters import GenreFilter
# Create your views here.


def home_page(request):

    searched = ''
    results = Games.objects.order_by('?')[:5]
    srchnum = 0
    if request.method == 'GET' and 'searched' in request.GET:
        searched = request.GET['searched']
        if searched is not None and searched != '':
            results = Games.objects.filter(title__unaccent__icontains=searched)
            for title in results:
                srchnum += 1
            context = {'searched':searched, 'results':results, 'srchnum':srchnum}
            return render(request, 'homepage.html', context)
        else:
            return render(request, 'homepage.html', {'searched':searched, 'results':results})
    else:
        return render(request, 'homepage.html', {'searched':searched, 'results':results})

# def test_page(request):
#     genre_filter = GenreFilter(request.GET, queryset=Games.objects.all())

#     usercollection = Collections.objects.filter(currentUser__exact=request.user.id)

#     context = {'test':usercollection}
#     return render(request, 'testpage.html', context)

# def search_game(request):
#     srchnum = 0
#     if 'searched' in request.GET:
#         searched = request.GET['searched']
#         results = Games.objects.filter(title__icontains=searched)

#         for title in results:
#             srchnum += 1

#         return render(request, 'search.html', {'searched':searched, 'results':results, 'srchnum':srchnum})
#     else:
#         return render(request, 'search.html')
    
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

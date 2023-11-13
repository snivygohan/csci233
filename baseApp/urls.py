from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    #path('search/', views.search_game, name='search'),
    path('addgame/', views.add_game, name='addgame'),
    path('filter/', views.filter_test, name='filter')
]
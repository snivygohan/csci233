from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('search/', views.search_game, name='search'),
    path('addgame/', views.add_game, name='addgame'),
    path('connect/(<operation>.+)/<int:id>/',views.changeCollection, name = 'changeCollection')
    
]
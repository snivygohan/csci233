from django.urls import path
from . import views

urlpatterns = [
    path('game/<int:id>/', views.games_page, name = 'game'),
    path('all/', views.all_games, name = 'all')
]

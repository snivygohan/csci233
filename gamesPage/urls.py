from django.urls import path
from . import views

#remember that you add "/games/" after whatever is there for the URL, and then continue the pathing.

urlpatterns = [
    path('library/', views.all_games, name = 'library'),
    path('game/<int:id>/', views.game_page, name = 'game'),
    path('addgame/', views.add_game, name = 'addgame'),
    path('removegame/', views.remove_game, name = 'removegame'),
    path('favgame/<int:id>/', views.favorite_game, name = 'favgame'),
    path('statusgame/<int:id>/', views.status_game, name = 'statusgame')
]

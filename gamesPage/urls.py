from django.urls import path
from . import views


#remember that you add "/games/" after whatever is there for the URL, and then continue the pathing.

urlpatterns = [
    path('all/', views.all_games, name = 'all'),
    path('game/<int:id>/', views.game_detail_view, name = 'game')
]

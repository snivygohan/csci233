from django.urls import path
from . import views
from .views import (gameView, gameDetailView)

#URL config
urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/',views.register_user, name='register'),
    path('profile/', views.profile, name = 'profile'),
    path('addgame/', views.add_game, name='addgame'),
    path("game", gameView.as_view(), name="game_list"),
    path('game/<int:pk>', gameDetailView.as_view(), name="game_detail"),
]

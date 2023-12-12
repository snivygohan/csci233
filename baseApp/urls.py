from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('addgame/', views.add_game, name='addgame')
]
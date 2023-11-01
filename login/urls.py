from django.urls import path
from . import views

#URL config
urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register_user, name='register'),
    path('addgame/', views.add_game, name='addgame')
]


from django.urls import path
from . import views

#URL config
urlpatterns = [
     path('profile/', views.profile, name = 'profilePage'),
     path(r'^connect/(?P<pk>)\d+/$', views.addToCollection, name = 'addToCollection')
 
]


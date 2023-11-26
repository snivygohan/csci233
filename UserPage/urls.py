from django.urls import path
from . import views
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static


#URL config
urlpatterns = [
     path('profile/<int:pk>/', views.profile, name = 'show_profile_page'),
     
     
     ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
=======

#URL config
urlpatterns = [
     path('profile/', views.profile, name = 'profilePage'),

 
]
>>>>>>> testSteve


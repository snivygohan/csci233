from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ShowProfilePageView

#URL config
urlpatterns = [
     path('<int:pk>/profile/',ShowProfilePageView.as_view, name = 'show_profile_page'),
     
 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


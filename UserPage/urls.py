from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


#URL config
app_name = "profile"
urlpatterns = [
     path('<int:pk>/', views.profile, name = 'profile'),
     path('search/', views.account_search_view, name= 'search'),
     
     
      ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



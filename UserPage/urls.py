from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


#URL config
urlpatterns = [
     path('<int:pk>/', views.profile, name = 'profile'),
     path('edit/<int:pk>',views.edit_account_view, name="edit"),
     
      ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



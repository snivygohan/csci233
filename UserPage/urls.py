from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


#URL config
urlpatterns = [
     path('<int:pk>/', views.profile, name = 'profile'),
     path('edit/<int:pk>',views.edit_account_view, name="edit"),
     path('fullCollection/<int:pk>', views.fullCollection, name = 'fullCollection'),
     path('favorites/<int:pk>', views.favorites, name = 'favorites'),
     path('current/<int:pk>', views.current, name = 'current'),
      path('finished/<int:pk>', views.finished, name = 'finished'),
     
      ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



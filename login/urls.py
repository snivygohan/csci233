from django.urls import path
from . import views

#URL config
urlpatterns = [
    path('login/', views.login_test),
]
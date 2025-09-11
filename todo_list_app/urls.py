from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # la page d'accueil de l'app
]
from django.urls import path # Import du module Path  
from .views import * # Import de notre fichier views

urlpatterns = [
    path("", home_view, name="home"),
]
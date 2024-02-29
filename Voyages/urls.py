# Dans urls.py pour l'application "voyages"
from django.urls import path
from . import views

app_name = 'Voyages'  # Définissez le nom de l'application pour éviter les conflits d'URL
urlpatterns = [
    path("", views.connexion, name="connexion"),
    path("register_user/", views.register_user, name='register_user'),
    path("home/", views.home, name='home' ),
]



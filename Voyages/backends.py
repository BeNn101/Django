from django.contrib.auth.backends import BaseBackend
from .models import Utilisateur

class UtilisateurBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Utilisateur.objects.get(username=username)
            if user.check_password(password):
                return user
        except Utilisateur.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Utilisateur.objects.get(pk=user_id)
        except Utilisateur.DoesNotExist:
            return None

from django.contrib import admin
from .models import Utilisateur, Voyage, Vol, Hebergement


admin.site.register(Utilisateur)
admin.site.register(Voyage)
admin.site.register(Vol)
admin.site.register(Hebergement)


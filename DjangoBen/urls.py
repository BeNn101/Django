
from django.contrib import admin
from django.urls import include,path
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView
urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy('Voyages:connexion'))),
    path("Voyages/", include("Voyages.urls")),
    path("admin/", admin.site.urls),
]

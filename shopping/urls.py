from django.contrib import admin
from django.urls import path
from .views import index, afficher_produit

urlpatterns = [
    path('', index, name="e_commerce-index"),
    path('produit-<str:id_produit>/', afficher_produit, name="afficher-produit"),
]

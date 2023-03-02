from django.contrib import admin
from django.urls import path
from shopping.views import index, afficher_produit

urlpatterns = [
    path('', index, name="shopping-index"),
    path('produit-<str:id_produit>/', afficher_produit, name="afficher-produit"),
]

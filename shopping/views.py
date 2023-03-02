from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # produits = Produit.objects.all()
    # return render(request, "shopping/index.html", context={"produits" : produits})
    return render(request, "shopping/index.html", context={"date" : datetime.today()})

def afficher_produit(request, id_produit):
    print(id_produit)
    return render(request, "shopping/produit/show.html", context={"date" : datetime.today()})

def payer_produit():
    return render(request, "shopping/produit/payer.html", context={"date" : datetime.today()})

def ajouter_au_panier():
    return render(request, "shopping/panier/ajouter.html", context={"date" : datetime.today()})
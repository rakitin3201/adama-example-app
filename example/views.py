from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # produits = Produit.objects.all()
    # return render(request, "shopping/index.html", context={"produits" : produits})
    return render(request, "example/index.html", context={"date" : datetime.today()})
from django.shortcuts import render
from .models import *


# Create your views here.
def home(req):
    unggulan = ProdukUnggulan.objects.all()
    baru  = ProdukBaru.objects.all()

    return render(req, 'home.html', {"unggulan" : unggulan, "baru" : baru})

def products(req):
    data = SemuaProduk.objects.all()

    return render(req, 'products.html', {"data" : data})

def about(req):
    return render(req, 'about.html')
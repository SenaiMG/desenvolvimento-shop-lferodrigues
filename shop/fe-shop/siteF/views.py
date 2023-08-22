from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")
    
    
def carrinho(request):
    return render(request,"carrinho.html")


# Create your views here.

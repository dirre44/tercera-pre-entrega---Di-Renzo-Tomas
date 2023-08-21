from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import Template, Context, loader

# Create your views here.

def inicio(request):

    return render (request, "inicio.html")

def aniadir_carrito(request):

    return render (request, "carrito.html")

def aniadir_amigos(request):

    return render (request, "amigos.html")
    

def aniadir_biblioteca(request):
    
    return render (request, "biblioteca.html")
    
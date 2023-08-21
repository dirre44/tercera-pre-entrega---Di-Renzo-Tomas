from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import Template, Context, loader
from .forms import * 

# Create your views here.

def inicio(request):

    return render (request, "inicio.html")

def aniadir_carrito(request):
    formulario_carrito=Carrito_form()

    if request.method=="POST":        
        form=Carrito_form(request.POST)

        if form.is_valid():
            info=form.cleaned_data
            nombre=info["juego"]
            precio=info["precio"]
            juego=Carrito(juego=nombre, precio=precio)
            juego.save()
            return render (request, "carrito.html", {"formulario":formulario_carrito,"mensaje":f"{nombre} fue añadido al carrito"})
        else:
            return render (request, "carrito.html", {"formulario":formulario_carrito,"mensaje":"datos invalidos"})

    else:
        return render (request, "carrito.html", {"formulario":formulario_carrito})
        
def aniadir_amigos(request):
    formulario_amigos=Amigos_form()

    if request.method=="POST":
        form=Amigos_form(request.POST)

        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            usuario=info["usuario"]
            online=info["online"]
            nuevo_amigo=Lista_amigos(nombre=nombre, usuario=usuario, online=online)
            nuevo_amigo.save()
            return render (request, "amigos.html", {"formulario":formulario_amigos, "mensaje":f"\"{usuario}\" fue agregado"})
        else: 
            return render (request, "amigos.html", {"formulario":formulario_amigos, "mensaje":"datos invalidos"})
    else:
        return render (request, "amigos.html", {"formulario":formulario_amigos})
    
def aniadir_biblioteca(request):
    formulario_biblioteca=Biblioteca_form()

    if request.method=="POST":
        form=Biblioteca_form(request.POST)

        if form.is_valid():
            info=form.cleaned_data
            nombre=info["juego"]
            instalado=info["instalado"]
            juego=Biblioteca(juego=nombre,instalado=instalado)
            juego.save()
            return render (request, "biblioteca.html", {"formulario":formulario_biblioteca, "mensaje":f"{nombre} fue añadido a la biblioteca"})
        else:
            return render (request, "biblioteca.html", {"formulario":formulario_biblioteca,"mensaje":"datos invalidos"})
    else:
        return render (request, "biblioteca.html", {"formulario":formulario_biblioteca})
    
def busqueda_amigos (request):
    usuario=request.GET["usuario"]

    if usuario!="":
        amigos=Lista_amigos.objects.filter(usuario__icontains=usuario)
        return render (request, "busqueda_amigos.html", {"amigos":amigos})
    else:
        return render (request, "busqueda_amigos.html", {"mensaje": "no se ha ingresado nada"})


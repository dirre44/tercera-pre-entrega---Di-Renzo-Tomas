from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import Template, Context, loader
from .forms import * 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
        
class Biblioteca_listar (ListView):
    model=Biblioteca
    template_name="biblioteca_listar.html"

class Biblioteca_crear(CreateView):
    model=Biblioteca
    success_url=reverse_lazy("listar_biblioteca")
    fields = ["juego", "instalado"]

class Biblioteca_detalle(DetailView):
    model=Biblioteca
    template_name='biblioteca_detalle.html'

class Biblioteca_borrar(DeleteView):
    model=Biblioteca
    success_url=reverse_lazy("listar_biblioteca")

class Biblioteca_editar(UpdateView):
    model=Biblioteca
    success_url=reverse_lazy("listar_biblioteca")
    fields = ["juego", "instalado"]

def aniadir_amigos(request):
    formulario_amigos=Amigos_form()
    amigos=Lista_amigos.objects.all()
    if request.method=="POST":
        form=Amigos_form(request.POST)
        amigos=Lista_amigos.objects.all()
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            usuario=info["usuario"]
            online=info["online"]
            nuevo_amigo=Lista_amigos(nombre=nombre, usuario=usuario, online=online)
            nuevo_amigo.save()
            return render (request, "amigos.html", {"formulario":formulario_amigos, "mensaje":f"\"{usuario}\" fue agregado", "amigos":amigos})
        else: 
            return render (request, "amigos.html", {"formulario":formulario_amigos, "mensaje":"datos invalidos", "amigos":amigos})
    else:
        return render (request, "amigos.html", {"formulario":formulario_amigos, "amigos":amigos})

def eliminar_amigo (request, id):
    amigo=Lista_amigos.objects.get(id=id)
    amigo.delete()
    formulario_amigos=Amigos_form()
    amigos=Lista_amigos.objects.all()
    mensaje="Amigo eliminado!!"
    return render (request, "amigos.html", {"formulario":formulario_amigos, "amigos":amigos, "mensaje":mensaje})

def editar_amigo(request, id):
    amigo=Lista_amigos.objects.get(id=id)
    if request.method=="POST":
        form=Amigos_form(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            amigo.nombre=info["nombre"]
            amigo.usuario=info["usuario"]
            amigo.online=info["online"]
            amigo.save()
            amigos=Lista_amigos.objects.all()
            formulario_amigos=Amigos_form()
            mensaje="Usuario editado"
            return render (request, "amigos.html", {"formulario":formulario_amigos, "amigos":amigos, "mensaje":mensaje})
    else:
        amigo=Lista_amigos.objects.get(id=id)
        form_editar=Amigos_form(initial={"nombre":amigo.nombre, "usuario":amigo.usuario, "online":amigo.online})
        return render (request, "editar_amigo.html", {"formulario":form_editar, "amigo":amigo})
    pass
    
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


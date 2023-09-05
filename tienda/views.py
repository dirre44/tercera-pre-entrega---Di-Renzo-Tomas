from typing import Any, Dict
from .models import *
from .forms import * 
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def obtener_avatar(request):
    if request.user.is_authenticated:
        avatar= Avatar.objects.filter(user=request.user.id)
        if len(avatar) != 0:
            return avatar[0].imagen.url
        else:
            return '/media/avatares/default_avatar.png'
    else:
        return '/media/avatares/Empty.png'

def inicio(request):
    return render (request, "inicio.html",{'avatar':obtener_avatar(request)})

@login_required
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
            return render (request, "carrito.html", {"formulario":formulario_carrito,"mensaje":f"{nombre} fue añadido al carrito", 'avatar':obtener_avatar(request)})
        else:
            return render (request, "carrito.html", {"formulario":formulario_carrito,"mensaje":"datos invalidos", 'avatar':obtener_avatar(request)})

    else:
        return render (request, "carrito.html", {"formulario":formulario_carrito, 'avatar':obtener_avatar(request)})
        
class Biblioteca_listar (LoginRequiredMixin, ListView):
    model=Biblioteca
    template_name="biblioteca_listar.html"
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['avatar']=obtener_avatar(request)

class Biblioteca_crear(LoginRequiredMixin, CreateView):
    model=Biblioteca
    success_url=reverse_lazy("listar_biblioteca")
    fields = ["juego", "instalado"]

class Biblioteca_detalle(LoginRequiredMixin, DetailView):
    model=Biblioteca
    template_name='biblioteca_detalle.html'

class Biblioteca_borrar(LoginRequiredMixin, DeleteView):
    model=Biblioteca
    success_url=reverse_lazy("listar_biblioteca")

class Biblioteca_editar(LoginRequiredMixin, UpdateView):
    model=Biblioteca
    success_url=reverse_lazy("listar_biblioteca")
    fields = ["juego", "instalado"]

@login_required
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

@login_required
def eliminar_amigo (request, id):
    amigo=Lista_amigos.objects.get(id=id)
    amigo.delete()
    formulario_amigos=Amigos_form()
    amigos=Lista_amigos.objects.all()
    mensaje="Amigo eliminado!!"
    return render (request, "amigos.html", {"formulario":formulario_amigos, "amigos":amigos, "mensaje":mensaje})

@login_required
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
            return render (request, "amigos.html", {"formulario":formulario_amigos, "amigos":amigos, "mensaje":mensaje, 'avatar':obtener_avatar(request)})
    else:
        amigo=Lista_amigos.objects.get(id=id)
        form_editar=Amigos_form(initial={"nombre":amigo.nombre, "usuario":amigo.usuario, "online":amigo.online, 'avatar':obtener_avatar(request)})
        return render (request, "editar_amigo.html", {"formulario":form_editar, "amigo":amigo, 'avatar':obtener_avatar(request)})
    pass

@login_required  
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
            return render (request, "biblioteca.html", {"formulario":formulario_biblioteca, "mensaje":f"{nombre} fue añadido a la biblioteca", 'avatar':obtener_avatar(request)})
        else:
            return render (request, "biblioteca.html", {"formulario":formulario_biblioteca,"mensaje":"datos invalidos", 'avatar':obtener_avatar(request)})
    else:
        return render (request, "biblioteca.html", {"formulario":formulario_biblioteca, 'avatar':obtener_avatar(request)})

@login_required  
def busqueda_amigos (request):
    usuario=request.GET["usuario"]

    if usuario!="":
        amigos=Lista_amigos.objects.filter(usuario__icontains=usuario)
        return render (request, "busqueda_amigos.html", {"amigos":amigos, 'avatar':obtener_avatar(request)})
    else:
        return render (request, "busqueda_amigos.html", {"mensaje": "no se ha ingresado nada", 'avatar':obtener_avatar(request)})
    

def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu =info["username"]
            clave=info['password']
            usuario=authenticate(username=usu, password=clave)
            if usuario != None:
                login (request, usuario)
                mensaje= f'usuario "{usuario}" logeado correctamente'
                return render (request, 'inicio.html', {'mensaje': mensaje, 'avatar':obtener_avatar(request)})
        else:
            mensaje='datos invalidos'
            return render (request, 'login.html', {'formulario':form,'mensaje': mensaje, 'avatar':obtener_avatar(request)})
    else:
        form=AuthenticationForm()
        mensaje='ingrese usuario y contraseña'
    return render(request, 'login.html', {'formulario':form, 'mensaje':mensaje, 'avatar':obtener_avatar(request)})

def register_usuario(request):
    if request.method=='POST':
        form=register_usuario_form(request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            usu =info["username"]
            form.save()
            mensaje = f'usuario "{usu}" creado correctamente'
            return render (request, 'inicio.html', {'mensaje': mensaje, 'avatar':obtener_avatar(request)})
        else:
            mensaje='datos invalidos'
            return render (request, 'register.html', {'formulario':form,'mensaje': mensaje, 'avatar':obtener_avatar(request)})
    else:
        form=register_usuario_form()
        mensaje='ingrese nuevo usuario y contraseña'
        return render(request, 'register.html', {'formulario':form, 'mensaje':mensaje, 'avatar':obtener_avatar(request)})
    pass

def editar_usuario (request):
    usuario=request.user # el usuario SIEMPRE esta en el request
    if request.method=='POST':
        form=Editar_usuario_form(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.first_name=info['first_name']
            usuario.last_name=info['last_name']
            usuario.email=info['email']
            usuario.password1=info['password1']
            usuario.password2=info['password2']
            usuario.save()
            mensaje=f'Usuario "{usuario}" editado!'
            return render(request, 'inicio.html', {'mensaje':mensaje, 'nombre_usuario':usuario.username, 'avatar':obtener_avatar(request)})
        else:
            mensaje='datos invalidos'
            return render(request, 'editar_usuario.html', {'mensaje':mensaje, 'formulario':form, 'nombre_usuario':usuario.username, 'avatar':obtener_avatar(request)})
    else:
        form=Editar_usuario_form(instance=usuario)
        mensaje=''
        return render(request, 'editar_usuario.html', {'mensaje':mensaje, 'formulario':form, 'nombre_usuario':usuario.username, 'avatar':obtener_avatar(request)})

def agregar_avatar (request):
    if request.method=="POST":
        form=Avatar_form(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES['imagen'])
            avatar_viejo=Avatar.objects.filter(user=request.user)
            if len(avatar_viejo)>0:
                avatar_viejo[0].delete()
            avatar.save()
            formulario=Editar_usuario_form(instance=request.user)
            return render(request,"editar_usuario.html", {"mensaje": 'avatar agregado', 'avatar':obtener_avatar(request), 'formulario':formulario})
    else:
        form=Avatar_form(request.POST)
        return render(request, 'agregar_avatar.html', {'formulario':form, 'usuario':request.user.username})
    pass



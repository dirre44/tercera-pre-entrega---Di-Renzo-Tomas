from .views import *
from django.urls import path

urlpatterns = [
    path('', inicio, name="inicio"),
    path("biblioteca/", aniadir_biblioteca, name="aniadir_biblioteca"),
    path("amigos/", aniadir_amigos, name="aniadir_amigos"),
    path("carrito/", aniadir_carrito, name="aniadir_carrito")
]
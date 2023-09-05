from .views import *
from django.urls import path

urlpatterns = [
    path('', inicio, name="inicio"),
    path("biblioteca/", aniadir_biblioteca, name="aniadir_biblioteca"),
    path("amigos/", aniadir_amigos, name="aniadir_amigos"),
    path("carrito/", aniadir_carrito, name="aniadir_carrito"),
    path("busqueda_amigos/", busqueda_amigos, name="buscar_amigos"),
    path("eliminar_amigo/<id>", eliminar_amigo, name="eliminar_amigo"),
    path("editar_amigo/<id>", editar_amigo, name="editar_amigo"),

    path("biblioteca_listar/", Biblioteca_listar.as_view(), name="listar_biblioteca"),
    path("biblioteca_crear/", Biblioteca_crear.as_view(), name="biblioteca_crear"),
    path("biblioteca_detalle/<pk>", Biblioteca_detalle.as_view(), name="biblioteca_detalle"),
    path("biblioteca_borrar/<pk>", Biblioteca_borrar.as_view(), name="biblioteca_borrar"),
    path("biblioteca_editar/<pk>", Biblioteca_editar.as_view(), name="biblioteca_editar"),

    # LOGIN, LOGOUT, REGISTER
    path("login/", login_request, name="login"),
    path("register/", register_usuario, name="registro"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("editar_usuario/", editar_usuario, name="editar_usuario"),

    path("agregar_avatar/", agregar_avatar, name="agregar_avatar")

]
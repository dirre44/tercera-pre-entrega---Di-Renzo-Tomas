from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Carrito (models.Model):
    juego = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.juego} - {self.precio}"
    
class  Biblioteca (models.Model):
    juego = models.CharField(max_length=50)
    instalado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.juego} - {self.instalado}"

class Lista_amigos (models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    online = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.usuario} - {self.online}"

class Avatar(models.Model):
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'imagen de {self.user}'
from django import forms

class Carrito_form(forms.Form):
    juego=forms.CharField(max_length=50)
    precio=forms.IntegerField()

class Amigos_form(forms.Form):
    nombre=forms.CharField(max_length=50)
    usuario=forms.CharField(max_length=50)
    online=forms.BooleanField()

class Biblioteca_form(forms.Form):
    juego=forms.CharField(max_length=50)
    instalado=forms.BooleanField()
from django import forms

class Carrito_form(forms.Form):
    juego=forms.CharField(max_length=50)
    precio=forms.IntegerField(required=False)

class Amigos_form(forms.Form):
    nombre=forms.CharField(max_length=50)
    usuario=forms.CharField(max_length=50)
    online=forms.BooleanField(required=False)

class Biblioteca_form(forms.Form):
    juego=forms.CharField(max_length=50)
    instalado=forms.BooleanField(required=False)
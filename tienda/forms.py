from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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

class register_usuario_form(UserCreationForm):
    email=forms.EmailField(label='Email usuario')
    password1=forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields={'username', 'email', 'password1', 'password2'}
        help_texts= { k:'' for k in fields }
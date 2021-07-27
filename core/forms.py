from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import nuevoUsuario
from .models import animales
from .models import compras

class CuentaForm(ModelForm):
    class Meta:
        model = nuevoUsuario
        fields = ['idUsuario','nombre','apellido','correo','clave']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'clave': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        
class validarUsuario(ModelForm):
    class Meta:
        model = nuevoUsuario
        fields = ['correo','clave']
        widgets = {
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'clave': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class animalesForm(ModelForm):
    class Meta:
        model = animales
        fields = ['idAnimal','animal']
        widgets = {
            'animal': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ComprasForm(ModelForm):
    class Meta:
        model = compras
        fields = ['idCompra','descripcion','precio','animales']
        widgets = {
            'animales': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),       
        }
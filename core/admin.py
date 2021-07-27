from django.contrib import admin
from . models import nuevoUsuario, animales, compras

# Register your models here.

admin.site.register(nuevoUsuario)
admin.site.register(animales)
admin.site.register(compras)
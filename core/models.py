from django.db import models
from django.db.models.fields import AutoField

# Create your models here.

class nuevoUsuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    clave = models.CharField(max_length=25)

    def __str__(self):
        return self.correo

class animales(models.Model):
    idAnimal = models.AutoField(primary_key=True)
    animal = models.CharField(max_length=30)

    def __str__(self):
        return self.animal 



class compras(models.Model):
    idCompra = models.AutoField(primary_key=True)
    animales = models.ForeignKey(animales, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.descripcion
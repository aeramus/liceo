import django
from django.db import models
from django.utils import timezone


class Cursos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return (self.nombre)

class Alumnos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def __str__(self):
        return (self.nombre + " " + self.apellido)
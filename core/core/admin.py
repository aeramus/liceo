from django.contrib import admin
from .models import *
# Register your models here.

class TablaCursos(admin.ModelAdmin):
    list_display= ('id','nombre')
    verbose_name = "Curso"
    verbose_name_plural = "Cursos"

class TablaAlumnos(admin.ModelAdmin):
    list_display= ('id','nombre','apellido','fecha_nacimiento','curso')
    verbose_name = "Alumno"
    verbose_name_plural = "Alumnos"

admin.site.register(Cursos,TablaCursos)
admin.site.register(Alumnos,TablaAlumnos)


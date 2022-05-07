from select import select
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import * 
from django.http import JsonResponse, FileResponse, HttpResponse
from django.shortcuts import redirect
from django.db.models import Q
from django.core.serializers import serialize

def index(request):
    
    return HttpResponse("Hola mundo")
    
def alumnos(request):

    if request.GET.get('id'):
        id = request.GET.get('id')
        alumnos = Alumnos.objects.filter(curso=id)
    else:
        alumnos = Alumnos.objects.all()

    cursos = Cursos.objects.all()
    
    return render(request, 'alumnos.html', {'datos': alumnos, 'cursos': cursos})
from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.

def padre_dato(request):

	nombresito = Padre(nombre = 'Jose', fecha_nacimiento = '1965-07-07', edad = 59)
	nombresito.save()	
	cadena_texto = f'Padre guardado: Nombre: {nombresito.nombre}, Fecha de nacimiento = {nombresito.fecha_nacimiento}, Edad = {nombresito.edad}'
	return HttpResponse(cadena_texto)


def padre(request):
	return HttpResponse('Esto es una vista del padre')

def madre(request):
	return HttpResponse('Esto es una vista de la madre')	

def hermano(request):
	return HttpResponse('Esto es una vista del hermano')	


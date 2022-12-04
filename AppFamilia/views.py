from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.

def padre(request):
	return HttpResponse('Esto es una vista del padre')

def madre(request):
	return HttpResponse('Esto es una vista de la madre')	

def hermano(request):
	return HttpResponse('Esto es una vista del hermano')	


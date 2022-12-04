from django.http import HttpResponse	# funcion que responde de forma rápida
from django.template import Template, Context, loader
from django.shortcuts import render

def familia(request):
	return HttpResponse('Usted tiene un padre, una madre y un hermano')


def prueba_html(request):
	diccionario = {'Padre':'Juan', 'Madre':'Lucia', 'Hermano': 'Jorge'}	
	archivo = open('/Users/rodrigohecht/Desktop/CoderHouse - Python/Proyectos/MVT Rodrigo Hecht/MVTRH/Plantillas/template_familia.html')
	template = Template(archivo.read())	#convierto mi archivo en un template
	archivo.close()	#los archivos hay que cerrarlos
	contexto = Context(diccionario)	#Sirve para ir llenando datos en la url
	documento=template.render(contexto)	# llename los espacios vacíos con los datos de contexto
	return HttpResponse(documento)
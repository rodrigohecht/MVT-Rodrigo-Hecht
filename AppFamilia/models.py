from django.db import models

# Create your models here.
    
class Padre(models.Model):
	nombre = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	edad = models.IntegerField()

class Madre(models.Model):
	nombre = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	edad = models.IntegerField()

class Hermano(models.Model):
	nombre = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	edad = models.IntegerField()




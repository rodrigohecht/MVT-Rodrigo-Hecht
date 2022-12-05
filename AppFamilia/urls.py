from django.urls import path
from . import views

urlpatterns = [
	path("padre/", views.padre),
	path("padre_dato/", views.padre_dato),
	path("madre", views.madre),
	path("hermano", views.hermano),
]

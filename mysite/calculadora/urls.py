# TRABAJO DE ANDREA
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('sumar/<int:numero1>/<int:numero2>', views.suma),
    path('restar/<int:numero1>/<int:numero2>', views.resta),
    path('multiplicar/<int:numero1>/<int:numero2>', views.multiplicacion),
    path('dividir/<int:numero1>/<int:numero2>', views.division),
]
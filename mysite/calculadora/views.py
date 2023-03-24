# TRABAJO DE ANDREA
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a tu calculadora digital.")

def suma(request, numero1, numero2):
    result = int(numero1) + int(numero2)
    return HttpResponse(f"La suma de {numero1} + {numero2} = {result}")


def resta(request, numero1, numero2):
    result = int(numero1)-(numero2)
    return HttpResponse(f"La resta de {numero1} - {numero2} = {result}")

def multiplicacion(request, numero1, numero2):
     result = int(numero1)*(numero2)
     return HttpResponse(f"El producto de {numero1} x {numero2} = {result}")

def division(request, numero1, numero2):
    try:
        result = int(numero1)/(numero2)
    except ZeroDivisionError:
        result = "No se puede dividir !ERROR!"
    return HttpResponse(f"El cociente de {numero1} / {numero2} = {result}")

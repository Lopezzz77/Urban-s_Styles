from urllib import request
from django.shortcuts import render
from .forms import FormularioRegistro

def Home(request):
    return render(request, 'index.html')

def Registrar(request):
   data = {
        'form': FormularioRegistro()
    }
   
   return render(request, 'Pages/registrar.html',data)
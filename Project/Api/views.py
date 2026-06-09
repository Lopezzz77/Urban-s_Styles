from urllib import request
from django.shortcuts import render

from Project.Api.models import Producto
from .forms import FormularioRegistro

def Home(request):
    return render(request, 'index.html')

def Registrar(request):
    data = {
        'form': FormularioRegistro()
    }
    if request.method=="POST":
        query=FormularioRegistro(data=request.POST,files=request.FILES)
        if query.is_valid():
            query.save()
            data["Mensaje"]="Datos Registrados"
            
        else:
            data['Formulario']="NO SE PUEDE REGISTRAR"
    return render(request, 'Pages/registrar.html',data)





def VerProductos(request):
    query=Producto.objects.all()
    data={
        'Productos':query
    }
    return render(request, 'Pages/verProductos.html', data)
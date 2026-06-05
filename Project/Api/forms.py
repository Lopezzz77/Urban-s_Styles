from .models import *
from django import forms

class FormularioRegistro(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
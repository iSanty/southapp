from django.shortcuts import render
from django.views.generic.edit import CreateView

from transportes.models import Transportes
from .forms import EnvioDatos

# Create your views here.


class CrearTransporte(CreateView):
    model = Transportes
    template_name = 'index.html'
    success_url = 'index.html'
    fields = ['dominio', 'nombre', 'apellido', 'imagen1', 'imagen2', 'imagen3', 'imagen4', 'imagen5', 'imagen6', 'imagen7']
    
    
    
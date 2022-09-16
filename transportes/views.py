from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from transportes.forms import FormBusquedaTransporte


from transportes.models import Transportes

# Create your views here.

class CrearTransporte(CreateView):
    model = Transportes
    template_name = 'transportes/transportes.html'
    success_url = '/transportes'
    fields = ['dominio', 'nombre', 'apellido', 'imagen1', 'imagen2', 'imagen3', 'imagen4', 'imagen5', 'imagen6', 'imagen7']
    
    
    
class VerTransporte(ListView):
    model = Transportes
    template_name = 'transportes/ver_transportes.html'
    
    def get_queryset(self):
        dominio = self.request.GET.get('dominio', '')
        if dominio:
            object_list = self.model.objects.filter(dominio__icontains=dominio)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormBusquedaTransporte()
        return context
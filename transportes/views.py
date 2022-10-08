from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from transportes.forms import FormBusquedaTransporte
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from . import models


from transportes.models import Transportes

# Create your views here.

@login_required
def mandarafreirchurros(request):
    return redirect('https://epresis.southpost.com.ar/')


class CrearTransporte(LoginRequiredMixin, CreateView):
    model = Transportes
    template_name = 'transportes/transportes.html'
    success_url = '/transportes'
    fields = ['dominio', 'nombre', 'apellido', 'imagen1', 'imagen2', 'imagen3', 'imagen4', 'imagen5', 'imagen6', 'imagen7']
    
    
    
class VerTransporte(LoginRequiredMixin, ListView):
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
    
@login_required
def ver_dominio(request, dominio):
    object_list = models.Transportes.objects.filter(id=dominio)
    return render(request, 'transportes/ver_dominio.html', {'object_list':object_list})
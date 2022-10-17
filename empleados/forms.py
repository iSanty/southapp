from django import forms

from empleados.models import Categoria


class FormAltaPersonalMeli(forms.Form):
    dni = forms.IntegerField()
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    
    
    
class FicharPersonalMeli(forms.Form):
    dni = forms.CharField(max_length=10)
    fecha_trabajada = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    categoria = forms.ModelChoiceField(queryset= Categoria.objects.all())
    
    
    
class CrearCategoria(forms.Form):
    categoria = forms.CharField(max_length=25)
    tarifa_por_dia = forms.FloatField()
    
    
    
class FormBusquedaFichero(forms.Form):
    dni = forms.IntegerField()
    
    
class FormEditarFicha(forms.Form):
    fecha_trabajada = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    dni = forms.IntegerField()
    categoria = forms.ModelChoiceField(queryset= Categoria.objects.all())
    tarifa = forms.FloatField()

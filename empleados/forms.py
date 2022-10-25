from django import forms

from empleados.models import Categoria, TipoTarifa, Sucursal


class FormVerPersonal(forms.Form):
    dni = forms.IntegerField(required=False)
    sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.all(), required=False)


class FormAltaPersonalMeli(forms.Form):
    dni = forms.IntegerField()
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    banco = forms.CharField(max_length=50)
    cbu = forms.CharField(max_length=22, required=False)
    alias = forms.CharField(max_length=50, required=False)
    sucursal_por_defecto = forms.ModelChoiceField(queryset= Sucursal.objects.all(), required=False)
    
    
    
class FicharPersonalMeli(forms.Form):
    dni = forms.CharField(max_length=10)
    fecha_trabajada = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    categoria = forms.ModelChoiceField(queryset= Categoria.objects.all())
    tipo_tarifa = forms.ModelChoiceField(queryset= TipoTarifa.objects.all(), required=False)
    sucursal = forms.ModelChoiceField(queryset= Sucursal.objects.all(), required=False)
    
    
    
class CrearCategoria(forms.Form):
    categoria = forms.CharField(max_length=25)
    tarifa_por_dia = forms.FloatField()
    
    
class FormTipoTarifa(forms.Form):
    tipo = forms.CharField(max_length=10)
    valor = forms.FloatField()
    
    
class FormBusquedaFichero(forms.Form):
    dni = forms.IntegerField(required=False)
    fecha_desde = forms.DateTimeField(input_formats=['%d/%m/%Y'], required=False)
    fecha_hasta = forms.DateTimeField(input_formats=['%d/%m/%Y'], required=False)
    sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.all(), required=False)
    
    
    
    
class FormEditarFicha(forms.Form):
    fecha_trabajada = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    dni = forms.IntegerField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    tarifa = forms.FloatField()
    sucursal = forms.CharField(max_length=30)



class FormSucursal(forms.Form):
    sucursal = forms.CharField(max_length=30)
    
    
    
class FormBuscarCategoria(forms.Form):
    categoria = forms.CharField(max_length=30, required=False)
    
class FormBuscarTarifa(forms.Form):
    tipo = forms.CharField(max_length=30, required=False)
    
class FormBuscarSucursal(forms.Form):
    sucursal = forms.CharField(max_length=30, required=False)
    
    
    
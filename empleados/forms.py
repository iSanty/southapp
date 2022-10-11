from django import forms


class FormAltaPersonalMeli(forms.Form):
    dni = forms.IntegerField()
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    
    
    
class FicharPersonalMeli(forms.Form):
    dni = forms.CharField(max_length=10)
    fecha_trabajada = forms.DateTimeField()
    categoria = forms.CharField(max_length=25)
    
    
    
class CrearCategoria(forms.Form):
    categoria = forms.CharField(max_length=25)
    tarifa_por_dia = forms.FloatField()
    
    
    
class FormBusquedaFichero(forms.Form):
    dni = forms.IntegerField()
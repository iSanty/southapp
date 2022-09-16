from django import forms


class EnvioDatos(forms.Form):
    dominio = forms.CharField(label='Dominio', max_length=30)
    nombre = forms.CharField(label='Nombre', max_length=30)
    apellido = forms.CharField(label='Apellido', max_length=30)
    imagen1 = forms.ImageField(required=True)
    imagen2 = forms.ImageField(required=True)
    imagen3 = forms.ImageField(required=True)
    imagen4 = forms.ImageField(required=True)
    imagen5 = forms.ImageField(required=True)
    imagen6 = forms.ImageField(required=True)
    imagen7 = forms.ImageField(required=True)
    
    
    
class FormBusquedaTransporte(forms.Form):
    dominio = forms.CharField(max_length=15)
from django import forms
from operaciones.models import Cia
from .models import PersonalDeposito, SubClientes, SectorDepo


class FormNuevoPK(forms.Form):
    numero = forms.IntegerField()
    cliente = forms.ModelChoiceField(queryset=Cia.objects.all())
    sub_cliente = forms.ModelChoiceField(queryset=SubClientes.objects.all())
    unidades = forms.IntegerField()
    fecha_procesado = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    hora_procesado = forms.CharField(required=False)
    
    
class FormFinalizarPK(forms.Form):
    numero = forms.IntegerField()
    operario = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all())
    fecha_picking = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    hora_inicio_picking = forms.CharField(required=False)
    hora_fin_picking =forms.CharField(required=False)
    
    
class FormSubCliente(forms.Form):
    codigo = forms.CharField()
    cia_asociada = forms.ModelChoiceField(queryset=Cia.objects.all())
    razon_social = forms.CharField()
    
    
class FormPersonalDeposito(forms.Form):
    dni = forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    sector = forms.ModelChoiceField(queryset=SectorDepo.objects.all())
    
 
    
class FormSector(forms.Form):
    descripcion = forms.CharField()
    
    
class FormFinalizarArm(forms.Form):
    numero = forms.IntegerField()
    fecha_armado = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    hora_fin_armado = forms.CharField(required=False)
    
from django import forms
from operaciones.models import Cia
from .models import PersonalDeposito, SubClientes, SectorDepo


class FormNuevoPK(forms.Form):
    numero = forms.IntegerField()
    cliente = forms.ModelChoiceField(queryset=Cia.objects.all())
    sub_cliente = forms.ModelChoiceField(queryset=SubClientes.objects.all().order_by('razon_social'))
    tipo = forms.CharField()
    unidades = forms.IntegerField()
    fecha_procesado = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    hora_procesado = forms.CharField(max_length=8)
    
    
class FormIniciarPK(forms.Form):
    numero = forms.IntegerField()
    iniciado_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    fecha_inicio_picking = forms.DateTimeField(input_formats=['%d/%m/%Y'])




class FormFinalizarPK(forms.Form):
    numero = forms.IntegerField()
    operario = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    fecha_picking = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    
    
    
class FormSubCliente(forms.Form):
    codigo = forms.CharField()
    cia_asociada = forms.ModelChoiceField(queryset=Cia.objects.all().order_by('descripcion'))
    razon_social = forms.CharField()
    
    
class FormPersonalDeposito(forms.Form):
    dni = forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    sector = forms.ModelChoiceField(queryset=SectorDepo.objects.all().order_by('descripcion'))
    
 
    
class FormSector(forms.Form):
    descripcion = forms.CharField()
    
    
class FormFinalizarArm(forms.Form):
    numero = forms.IntegerField()
    finalizado_arm_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    contribuyentes = forms.IntegerField()
    fecha_finalizado_armado = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    
    
class FormIniciarArm(forms.Form):
    numero = forms.IntegerField()
    fecha_armado = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    inicio_arm_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    
    
class FormEditarGlobal(forms.Form):
    numero = forms.IntegerField()
    cliente = forms.CharField() #agarro de operaciones
    sub_cliente = forms.CharField()
    tipo = forms.CharField()
    unidades = forms.IntegerField()
    fecha_creacion = forms.DateField(input_formats=['%d/%m/%Y'])
    fecha_procesado = forms.DateField(input_formats=['%d/%m/%Y'])
    hora_procesado = forms.CharField()
    
    #esta parte es la que llena el administrativo
    
    operario = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    fecha_picking = forms.DateField(input_formats=['%d/%m/%Y'])#fecha en la que finaliza el picking
    fecha_inicio_picking = forms.DateField(input_formats=['%d/%m/%Y'])
    hora_inicio_picking = forms.CharField()
    iniciado_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    hora_fin_picking = forms.CharField()
    usuario_inicio = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    finalizado_pk_por = forms.CharField()
    
    fecha_armado = forms.DateField(input_formats=['%d/%m/%Y'])
    fecha_finalizado_armado = forms.DateField(input_formats=['%d/%m/%Y'])
    hora_fin_armado = forms.CharField()
    hora_inicio_armado = forms.CharField()
    inicio_arm_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    contribuyentes = forms.IntegerField()
    finalizado_arm_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    usuario_inicio_arm = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    
    estado_picking = forms.CharField()
    estado_armado = forms.CharField()
    nombre_planilla = forms.CharField()
    
    en_picking = forms.CharField()
    en_armado = forms.CharField()
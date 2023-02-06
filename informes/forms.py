from django import forms
from operaciones.models import Cia
from .models import PersonalDeposito, SubClientes, SectorDepo, NombrePlanilla


class FormNuevoPK(forms.Form):
    numero = forms.IntegerField()
    # cliente = forms.ModelChoiceField(queryset=Cia.objects.all())
    # sub_cliente = forms.ModelChoiceField(queryset=SubClientes.objects.all().order_by('razon_social'))
    nombre_planilla = forms.ModelChoiceField(queryset=NombrePlanilla.objects.all().order_by('nombre'))
    tipo = forms.CharField()
    unidades = forms.IntegerField()
    fecha_procesado = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    hora_procesado = forms.TimeField()
    
    
class FormIniciarPK(forms.Form):
    numero = forms.IntegerField()
    iniciado_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    fecha_inicio_picking = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    hora = forms.TimeField()




class FormFinalizarPK(forms.Form):
    numero = forms.IntegerField()
    operario = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    fecha_picking = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    hora_inicio_pk = forms.TimeField()
    hora_fin_pk = forms.TimeField()
    
    
    
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
    
class FormNombrePlanilla(forms.Form):
    nombre = forms.CharField()
    
    
class FormFinalizarArm(forms.Form):
    numero = forms.IntegerField()
    
    contribuyentes = forms.IntegerField()
    fecha_finalizado_armado = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    hora_inicio_armado = forms.TimeField()
    hora_fin_armado = forms.TimeField()
    
    
class FormIniciarArm(forms.Form):
    numero = forms.IntegerField()
    fecha_armado = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    inicio_arm_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    hora = forms.TimeField()
    
    
class FormEditarGlobal(forms.Form):
    numero = forms.IntegerField()
    cliente = forms.CharField() #agarro de operaciones
    sub_cliente = forms.CharField()
    tipo = forms.CharField()
    unidades = forms.IntegerField()
    fecha_creacion = forms.DateField(input_formats=['%d/%m/%Y'])
    fecha_procesado = forms.DateField(input_formats=['%d/%m/%Y'])
    hora_procesado = forms.TimeField()
    
    #esta parte es la que llena el administrativo
    
    operario = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    fecha_picking = forms.DateField(input_formats=['%d/%m/%Y'])#fecha en la que finaliza el picking
    fecha_inicio_picking = forms.DateField(input_formats=['%d/%m/%Y'])
    hora_inicio_picking = forms.TimeField()
    iniciado_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    hora_fin_picking = forms.TimeField()
    usuario_inicio = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    finalizado_pk_por = forms.CharField()
    
    fecha_armado = forms.DateField(input_formats=['%d/%m/%Y'])
    fecha_finalizado_armado = forms.DateField(input_formats=['%d/%m/%Y'])
    hora_fin_armado = forms.TimeField()
    hora_inicio_armado = forms.TimeField()
    inicio_arm_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    contribuyentes = forms.IntegerField()
    finalizado_arm_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    usuario_inicio_arm = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'))
    
    estado_picking = forms.CharField()
    estado_armado = forms.CharField()
    nombre_planilla = forms.CharField()
    
    en_picking = forms.CharField()
    en_armado = forms.CharField()
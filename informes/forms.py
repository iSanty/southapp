from django import forms
from operaciones.models import Cia
from .models import PersonalDeposito, SubClientes, SectorDepo, NombrePlanilla, GlobalPK


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
    numero = forms.IntegerField(required=False)
    cliente = forms.CharField(required=False) #agarro de operaciones
    sub_cliente = forms.CharField(required=False)
    tipo = forms.CharField(required=False)
    unidades = forms.IntegerField(required=False)
    fecha_creacion = forms.DateField(input_formats=['%d/%m/%Y'], required=False)
    fecha_procesado = forms.DateField(input_formats=['%d/%m/%Y'], required=False)
    hora_procesado = forms.TimeField(required=False)
    
    #esta parte es la que llena el administrativo
    
    operario = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'), required=False)
    fecha_picking = forms.DateField(input_formats=['%d/%m/%Y'], required=False)#fecha en la que finaliza el picking
    fecha_inicio_picking = forms.DateField(input_formats=['%d/%m/%Y'], required=False)
    hora_inicio_picking = forms.TimeField()
    iniciado_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'), required=False)
    hora_fin_picking = forms.TimeField()
    usuario_inicio = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'), required=False)
    finalizado_pk_por = forms.CharField(required=False)
    
    fecha_armado = forms.DateField(input_formats=['%d/%m/%Y'], required=False)
    fecha_finalizado_armado = forms.DateField(input_formats=['%d/%m/%Y'], required=False)
    hora_fin_armado = forms.TimeField(required=False)
    hora_inicio_armado = forms.TimeField(required=False)
    inicio_arm_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'), required=False)
    contribuyentes = forms.IntegerField(required=False)
    finalizado_arm_por = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'), required=False)
    usuario_inicio_arm = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all().order_by('nombre'), required=False)
    
    estado_picking = forms.CharField(required=False)
    estado_armado = forms.CharField(required=False)
    nombre_planilla = forms.CharField(required=False)
    
    en_picking = forms.CharField(required=False)
    en_armado = forms.CharField(required=False)
    
    
    
class FormFiltroPlanilla(forms.Form):
    lista_fecha_1 = (
        ('Procesado', 'Procesado'),
        # ('Pickeo', 'Pickeo'),
        # ('Armado', 'Armado'), 
        ('Fin Pickeo', 'Fin Pickeo'), 
        ('Fin Armado', 'Fin Armado')
        )
    
    fecha_de = forms.ChoiceField(choices=lista_fecha_1)
    fecha_inicial = forms.DateField(input_formats=['%d/%m/%Y'])
    fecha_final = forms.DateField(input_formats=['%d/%m/%Y'])
    
    cliente = forms.ModelChoiceField(queryset=NombrePlanilla.objects.all().order_by('nombre'), required=False)
    picking = forms.IntegerField(required=False)
    operario = forms.ModelChoiceField(queryset=PersonalDeposito.objects.all(), required=False)
    lista_estados = (
        ("1", 'Todos'),
        ("PK Finalizado", 'PK Finalizado'),
        ("PK Pendiente", 'PK Pendiente'),
        ("ARM Finalizado", 'ARM Finalizado'),
        ("ARM Pendiente", 'ARM Pendiente')
        
    
        )
    estado_de = forms.ChoiceField(choices=lista_estados, required=False)
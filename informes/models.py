from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class GlobalPK(models.Model):
    numero = models.IntegerField()
    cliente = models.CharField(max_length=50) #agarro de operaciones
    sub_cliente = models.CharField(max_length=50)
    tipo = models.CharField(max_length=128)
    unidades = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    fecha_procesado = models.DateField(null=True)
    hora_procesado = models.TimeField(null=True)
    creado_por = models.CharField(max_length=128, null=0)
    #esta parte es la que llena el administrativo
    
    operario = models.CharField(max_length=20) #este campo es "finalizado por"
    fecha_picking = models.DateField(null=True)#fecha en la que finaliza el picking
    fecha_inicio_picking = models.DateField(null=True)
    hora_inicio_picking = models.TimeField(null=True)
    iniciado_por = models.CharField(max_length=20)
    hora_fin_picking = models.TimeField(null=True)
    usuario_inicio = models.CharField(max_length=128)
    finalizado_pk_por = models.CharField(max_length=128)
    
    fecha_armado = models.DateField(null=True)
    fecha_finalizado_armado = models.DateField(null=True)
    hora_fin_armado = models.TimeField(null=True)
    hora_inicio_armado = models.TimeField(null=True)
    inicio_arm_por = models.CharField(max_length=20)
    contribuyentes = models.IntegerField(null=True)
    finalizado_arm_por = models.CharField(max_length=20)
    usuario_inicio_arm = models.CharField(max_length=20)
    
    estado_picking = models.CharField(max_length=20)
    estado_armado = models.CharField(max_length=20)
    nombre_planilla = models.CharField(max_length=50)
    
    en_picking = models.CharField(max_length=128)
    en_armado = models.CharField(max_length=128)
    
    editado_por = models.CharField(max_length=20)
    fecha_edicion = models.DateField(null=True)
    cantidad_ediciones = models.IntegerField(null=True)
    
    
    
    
    def __str__(self):
        return f'{self.nombre_planilla}'
    
    
    # def calcular_dias(self, fecha_proceso):
    #     pendiente_armado = self.fecha_armado - fecha_proceso
    #     print(pendiente_armado)
    
    
    
    
class SubClientes(models.Model):
    codigo = models.CharField(max_length=128)
    cia_asociada = models.CharField(max_length=30)
    razon_social = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.razon_social}'
    
class PersonalDeposito(models.Model):
    dni = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    
class SectorDepo(models.Model):
    descripcion = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.descripcion}'
    
    
    
class Pendientes(models.Model):
    canal = models.CharField(max_length=100)
    pend_tres_o_mas = models.IntegerField(null=0)
    pend_dos = models.IntegerField(null=0)
    pend_uno = models.IntegerField(null=0)
    base_del_dia = models.IntegerField(null=0)
    finalizado = models.IntegerField(null=0)
    pendiente_para_sig_dia = models.IntegerField(null=0)
    
    def __str__(self):
        return f'{self.canal}, {self.pend_tres_o_mas}, {self.pend_dos}, {self.pend_uno}, {self.base_del_dia}, {self.finalizado}, {self.pendiente_para_sig_dia}'
    
    
    
class PendientesArm(models.Model):
    canal = models.CharField(max_length=100)
    pend_tres_o_mas = models.IntegerField(null=0)
    pend_dos = models.IntegerField(null=0)
    pend_uno = models.IntegerField(null=0)
    base_del_dia = models.IntegerField(null=0)
    finalizado = models.IntegerField(null=0)
    pendiente_para_sig_dia = models.IntegerField(null=0)
    
    def __str__(self):
        return f'{self.canal}, {self.pend_tres_o_mas}, {self.pend_dos}, {self.pend_uno}, {self.base_del_dia}, {self.finalizado}, {self.pendiente_para_sig_dia}'
    
    
class PendientePkPorDia(models.Model):
    fecha = models.DateField()
    unidades = models.IntegerField()
    
    
class PenditenteArmPorDia(models.Model):
    fecha = models.DateField()
    unidades = models.IntegerField()
    
    
class FinalizadoPkPorDia(models.Model):
    fecha = models.DateField()
    unidades = models.IntegerField()
    
    
class FinalizadoArmPorDia(models.Model):
    fecha = models.DateField()
    unidades = models.IntegerField()
    
    
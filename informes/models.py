from django.db import models

# Create your models here.



class GlobalPK(models.Model):
    numero = models.IntegerField()
    cliente = models.CharField(max_length=50) #agarro de operaciones
    sub_cliente = models.CharField(max_length=50)
    unidades = models.IntegerField()
    fecha_procesado = models.DateTimeField(null=True)
    hora_procesado = models.CharField(max_length=8, null=0)
    operario = models.CharField(max_length=20)
    fecha_picking = models.DateTimeField(null=True)
    fecha_armado = models.DateTimeField(null=True)
    hora_inicio_picking = models.CharField(max_length=8, null=0)
    hora_fin_picking = models.CharField(max_length=8, null=0)
    hora_fin_armado = models.CharField(max_length=8, null=0)
    estado_picking = models.CharField(max_length=20)
    estado_armado = models.CharField(max_length=20)
    nombre_planilla = models.CharField(max_length=50)
    
    
    
    
    def __str__(self):
        return f'{self.nombre_planilla}'
    
    
    # def calcular_dias(self, fecha_proceso):
    #     pendiente_armado = self.fecha_armado - fecha_proceso
    #     print(pendiente_armado)
    
    
    
    
class SubClientes(models.Model):
    codigo = models.CharField(max_length=6)
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
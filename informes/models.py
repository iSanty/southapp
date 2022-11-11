from django.db import models

# Create your models here.



class GlobalPK(models.Model):
    numero = models.IntegerField()
    cliente = models.CharField(max_length=50) #agarro de operaciones
    sub_cliente = models.CharField(max_length=50)
    unidades = models.IntegerField()
    fecha_procesado = models.DateTimeField()
    hora_procesado = models.CharField(max_length=8)
    operario = models.CharField(max_length=20)
    fecha_picking = models.DateTimeField()
    fecha_armado = models.DateTimeField()
    hora_inicio_picking = models.CharField(max_length=8)
    hora_fin_picking = models.CharField(max_length=8)
    hora_fin_armado = models.CharField(max_length=8)
    estado_picking = models.CharField(max_length=20)
    estado_armado = models.CharField(max_length=20)
    
    
    
    
    def __str__(self):
        return f'{self.numero} - {self.sub_cliente}'
    
    
    
class SubClientes(models.Model):
    codigo = models.CharField(max_length=6)
    cia_asociada = models.CharField(max_length=30)
    razon_social = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.codigo} - {self.razon_social}'
    
class PersonalDeposito(models.Model):
    dni = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} - {self.apellido}'
    
    
class SectorDepo(models.Model):
    descripcion = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.descripcion}'
    
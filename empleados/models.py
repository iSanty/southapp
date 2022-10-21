from email.policy import default
from django.db import models

# Create your models here.


class EmpleadoMeli(models.Model):
    dni = models.BigIntegerField(default=0)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    banco = models.CharField(max_length=50)
    cbu = models.CharField(max_length=22)
    alias = models.CharField(max_length=50)
    sucursal_por_defecto = models.CharField(max_length=50)
    
    alta_por = models.CharField(max_length=50)
    fecha_alta = models.DateTimeField(null=True)
    
    
    def __str__(self):
        return f'{self.dni}'
    
    
    
class Categoria(models.Model):
    categoria = models.CharField(max_length=25)
    tarifa_por_dia = models.FloatField(null=0)
    
    def __str__(self):
        return f'{self.categoria}'
    
    
    
class TipoTarifa(models.Model):
    tipo = models.CharField(max_length=10)
    valor = models.FloatField(null=0)
    
    def __str__(self):
        return f'{self.tipo}'
    
    
class Fichero(models.Model):
    fecha_trabajada = models.DateTimeField(null=True)
    dni = models.IntegerField(null=0)
    categoria = models.CharField(max_length=25)
    tarifa = models.FloatField(null=0)
    tipo_tarifa = models.CharField(max_length=10)
    suma_a_tarifa = models.FloatField(null=0)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    total_dia = models.FloatField(null=0)
    sucursal = models.CharField(max_length=50)
    creado_por = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(null=True)
    cbu = models.CharField(max_length=22)
    alias = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    editado = models.CharField(max_length=50)
    fecha_de_edicion = models.DateTimeField(null=True)
    pago_realizado = models.CharField(max_length=50)
    fecha_pago = models.DateTimeField(null=True)
    
    
    
class Sucursal(models.Model):
    sucursal = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.sucursal}'
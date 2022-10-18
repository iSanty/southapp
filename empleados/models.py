from django.db import models

# Create your models here.


class EmpleadoMeli(models.Model):
    dni = models.IntegerField(null=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre}'
    
    
    
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
    cantidad = models.IntegerField(null=0)
    categoria = models.CharField(max_length=25)
    tarifa = models.FloatField(null=0)
    tipo_tarifa = models.CharField(max_length=10)
    suma_a_tarifa = models.FloatField(null=0)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    total_dia = models.FloatField(null=0)
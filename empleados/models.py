from django.db import models

# Create your models here.


class EmpleadoMeli(models.Model):
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    fecha_trabajada = models.DateTimeField(null=True)
    cantidad = models.FloatField(null=1)
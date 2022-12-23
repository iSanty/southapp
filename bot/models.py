from django.db import models

# Create your models here.


class Accion(models.Model):
    numero = models.CharField(max_length=128)
    accion = models.CharField(max_length=128)
    
    def __str__(self):
        return f'{self.accion}'
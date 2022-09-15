from django.db import models

# Create your models here.
class Transportes(models.model):
    dominio = models.CharField(max_length=30)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    imagen1 = models.ImageField(upload_to='camionetas', null=True, blank =True)
    imagen2 = models.ImageField(upload_to='camionetas', null=True, blank =True)
    imagen3 = models.ImageField(upload_to='camionetas', null=True, blank =True)
    imagen4 = models.ImageField(upload_to='camionetas', null=True, blank =True)
    imagen5 = models.ImageField(upload_to='camionetas', null=True, blank =True)
    imagen6 = models.ImageField(upload_to='camionetas', null=True, blank =True)
    imagen7 = models.ImageField(upload_to='camionetas', null=True, blank =True)
    
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Accion(models.Model):
    numero = models.CharField(max_length=128)
    accion = models.CharField(max_length=128)
    
    def __str__(self):
        return f'{self.accion}'
    
    
    
class MensajePorEstado(models.Model):
    estado = models.CharField(max_length=128)
    mensaje = RichTextField(max_length=256)
    
    def __str__(self):
        return f'{self.mensaje}'
    
    
    
class MailParaElBot(models.Model):
    mail = models.EmailField(max_length=254)
    
    
    def __str__(self):
        return f'{self.mail}'
    
    
    

class GrupoMSJ(models.Model):
    grupo = models.CharField(max_length=128)
    
    def __str__(self):
        return f'{self.grupo}'
    
    
    
    
class ClienteAtendido(models.Model):
    numero_cel = models.CharField(max_length=20)
    nivel_satisfaccion = models.IntegerField()
    guia_consultada = models.CharField(max_length=12)
    estado_de_guia_consultada = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.numero_cel}'
    
    
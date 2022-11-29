from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

# Create your models here.


class InformePreparacion(TimeStampedModel, SoftDeletableModel):
    numero = models.IntegerField(null=False)
    sub_cliente = models.CharField(max_length=50, null=False)
    unidades = models.IntegerField(null=False)
    estado = models.CharField(max_length=50, null=False)
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="fecha")
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.numero
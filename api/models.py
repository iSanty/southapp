from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

# Create your models here.


class Guia(models.Model):
    nro_guia = models.CharField(max_length=256)
    remito = models.CharField(max_length=256)
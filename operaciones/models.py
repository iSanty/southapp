
from django.db import models

from django.contrib.auth.models import User

class Producto(models.Model):
    
    cia = models.CharField(max_length=3)
    codigo = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=180)
    peso_un = models.FloatField(null=0)
    largo_un = models.FloatField(null=0)
    ancho_un = models.FloatField(null=0)
    alto_un = models.FloatField(null=0)
    unidad_caja = models.IntegerField(null=0)
    largo_cj = models.FloatField(null=0)
    ancho_cj = models.FloatField(null=0)
    alto_cj = models.FloatField(null=0)
    unidad_pall = models.IntegerField(null=0)
    pack = models.CharField(max_length=15)
    vd = models.FloatField(null=0)
    tipo_alm = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(null=True)
    usuario = models.CharField(max_length=180)

    cat_ub = models.CharField(max_length=3)
    cat_pk = models.CharField(max_length=3)
    cat_repo = models.CharField(max_length=3)
    cat_emb = models.CharField(max_length=3)
    clase = models.CharField(max_length=1) #siempre B
    unidad_minima = models.IntegerField(null=1) #siempre 1
    unidad_medida = models.CharField(max_length=180, null='01') #siempre 01
    peso_cj = models.FloatField(null=0) #multiplicacion de peso * unidad_caja
    peso_pall = models.FloatField(null=0) #multiplicacion de peso * unidad_pall
    
    largo_pall = models.CharField(max_length=180, null='1,2')
    ancho_pall = models.CharField(max_length=180, null='1')
    alto_pall = models.CharField(max_length=180, null='1,4')
    
    importado_saad = models.CharField(max_length=2, null='No') #si o no 'para importar solo lo que hace falta en saad
    importado_presis = models.CharField(max_length=2, null='No') #si o no 'para importar solo lo que hace falta en saad
    
    def __str__(self):
        return f'{self.codigo}'
    
    
    
class Cia(models.Model):
    cod = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.cod}'
    
    
class CatUbicacion(models.Model):
    cod = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.cod}'
    
    
class CatPicking(models.Model):
    cod = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.cod}'
    
    
class CatRepo(models.Model):
    cod = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.cod}'
    
    
class TipoAlm(models.Model):
    descripcion = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.cod}'
    
    
    
class TipoPack(models.Model):
    desc = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.cod}'
    
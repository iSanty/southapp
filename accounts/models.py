from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class MasDatosUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank =True)
    descripcion = RichTextField(null=True)
    sucursal = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.user}'
    

from django.contrib import admin
from .models import EmpleadoMeli, Categoria, Fichero


# Register your models here.
admin.site.register(EmpleadoMeli)
admin.site.register(Categoria)
admin.site.register(Fichero)
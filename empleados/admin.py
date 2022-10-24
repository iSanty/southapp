from django.contrib import admin
from .models import EmpleadoMeli, Categoria, Fichero, TipoTarifa, Sucursal


# Register your models here.
admin.site.register(EmpleadoMeli)
admin.site.register(Categoria)
admin.site.register(Fichero)
admin.site.register(TipoTarifa)
admin.site.register(Sucursal)
from django.contrib import admin
from .models import CatUbicacionValor, Cia, Producto, TipoPack, CatUbicacion, CatPicking, CatRepo, TipoAlm, Cubicaje
# Register your models here.
admin.site.register(Producto)
admin.site.register(Cia)

admin.site.register(CatUbicacion)
admin.site.register(CatPicking)
admin.site.register(CatRepo)
admin.site.register(CatUbicacionValor)
admin.site.register(TipoAlm)
admin.site.register(TipoPack)
admin.site.register(Cubicaje)

# Register your models here.

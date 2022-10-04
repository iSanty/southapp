
from django.urls import path
from . import views



urlpatterns = [
    
    # path('nuevo_aforo/', views.nuevo_aforo, name='nuevo_aforo'),
    path('nuevo_aforo/', views.nuevo_aforo, name='nuevo_aforo'),
    path('exportar_saad/', views.exportar_saad, name='exportar_saad'),
    path('crear_cia/', views.CrearCia.as_view(), name='crear_cia'),
    path('ver_productos/', views.ver_productos, name='ver_productos'),
    path('editar_producto/<int:id>/', views.editar_producto, name = 'editar_producto'),
    

]


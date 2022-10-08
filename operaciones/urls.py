
from django.urls import path
from . import views
from SouthApp.views import index



urlpatterns = [
    
    
    path('deposito/', views.index_deposito, name='index_deposito'),
    path('nuevo_aforo/', views.nuevo_aforo, name='nuevo_aforo'),
    path('parametros/', views.crear_parametros, name='crear_parametros'),
    path('exportar_saad/', views.exportar_saad, name='exportar_saad'),
    path('exportar_presis/', views.exportar_presis, name='exportar_presis'),
    path('ver_productos/', views.ver_productos, name='ver_productos'),
    path('editar_producto/<int:id>/', views.editar_producto, name = 'editar_producto'),
    path('crear_parametros/', views.crear_parametros, name = 'crear_parametros'),
    

]


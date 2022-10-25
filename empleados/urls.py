from django.urls import path
from .views import EliminarCategoria, EliminarSucursal, EliminarTarifa, alta_personal_meli, edicion_fichero, editar_personal, editar_sucursal, index_meli, linkeo, alta_categoria, fichero, busqueda_fichero, ver_personal, ver_parametros, editar_categoria, editar_tarifa

urlpatterns = [
    
    path('', linkeo, name='linkeo'), #aca entro por /empleados por que es el unico acceso de la pag de sp .com.ar
    
    path('meli/', index_meli, name='index_meli'),
    path('alta_personal_meli/', alta_personal_meli, name='alta_personal_meli'),
    path('crear_categoria/', alta_categoria, name='crear_categoria'),
    path('fichero/', fichero, name='fichero'),
    path('busqueda_fichero/', busqueda_fichero, name='busqueda_fichero'),
    path('edicion_ficha/<int:id>/', edicion_fichero, name = 'edicion_ficha'),
    path('editar_personal/<int:id>/', editar_personal, name = 'editar_personal'),
    path('ver_personal/', ver_personal, name = 'ver_personal'),
    path('ver_parametros/', ver_parametros, name = 'ver_parametros'),
    path('editar_categoria/<int:id>/', editar_categoria , name = 'editar_categoria'),
    path('editar_tarifa/<int:id>/', editar_tarifa , name = 'editar_tarifa'),
    path('editar_sucursal/<int:id>/', editar_sucursal , name = 'editar_sucursal'),
    path('eliminar_sucursal/<int:pk>/', EliminarSucursal.as_view() , name = 'eliminar_sucursal'),
    path('eliminar_categoria/<int:pk>/', EliminarCategoria.as_view() , name = 'eliminar_categoria'),
    path('eliminar_tarifa/<int:pk>/', EliminarTarifa.as_view() , name = 'eliminar_tarifa'),
    




]





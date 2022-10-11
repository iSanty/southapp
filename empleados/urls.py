from django.urls import path
from .views import alta_personal_meli, index_meli, linkeo, alta_categoria, fichero, editar_fichero

urlpatterns = [
    
    path('', linkeo, name='linkeo'), #aca entro por /empleados por que es el unico acceso de la pag de sp .com.ar
    
    path('meli/', index_meli, name='index_meli'),
    path('alta_personal_meli/', alta_personal_meli, name='alta_personal_meli'),
    path('crear_categoria/', alta_categoria, name='crear_categoria'),
    path('fichero/', fichero, name='fichero'),
    path('editar_fichero/', editar_fichero, name='editar_fichero'),

]


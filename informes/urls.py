from django.urls import path
from .views import index_informes, nuevo_global, parametros , finalizar_global, informe_global, finalizar_armado, editar_global, index_informes_2, inciar_picking, iniciar_armado


urlpatterns = [
    
    
    path('index2/', index_informes, name='index_informes'),
    path('', index_informes_2, name='index_informes2'),
    path('nuevo_global/', nuevo_global, name='nuevo_global'),
    path('informe_global/',informe_global , name='informe_global'),
    path('parametros/',parametros , name='parametros'),
    path('finalizar_global/', finalizar_global, name='finalizar_global'),
    path('finalizar_armado/', finalizar_armado, name='finalizar_armado'),
    path('editar_global/<int:id>/', editar_global, name='editar_global'),
    path('iniciar_picking/', inciar_picking, name='iniciar_picking'),
    path('iniciar_armado/', iniciar_armado, name='iniciar_armado'),
    
    



]



from django.urls import path
from .views import index_informes, nuevo_global, parametros , finalizar_global, informe_global, finalizar_armado


urlpatterns = [
    
    
    path('', index_informes, name='index_informes'),
    path('nuevo_global/', nuevo_global, name='nuevo_global'),
    path('informe_global/',informe_global , name='informe_global'),
    path('parametros/',parametros , name='parametros'),
    path('finalizar_global/', finalizar_global, name='finalizar_global'),
    path('finalizar_armado/', finalizar_armado, name='finalizar_armado'),
    



]

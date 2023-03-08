from django.urls import path
from .views import index_informes, nuevo_global, parametros , finalizar_global, informe_global, finalizar_armado, editar_global, index_informes_2, inciar_picking, iniciar_armado, detalle_base_dia, detalle_fin_arm, detalle_fin_pk, detalle_pend_arm, detalle_pend_pk, detalle_proc_arm, detalle_proc_pk, detalle_por_subcliente, monitor, consulta_planilla, detalle_picking_por_persona


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
    
    path('base_dia/', detalle_base_dia, name='base_dia'),
    path('detalle_fin_arm/', detalle_fin_arm, name='detalle_fin_arm'),
    path('detalle_fin_pk/', detalle_fin_pk, name='detalle_fin_pk'),
    path('detalle_pend_arm/', detalle_pend_arm, name='detalle_pend_arm'),
    path('detalle_picking_por_persona/', detalle_picking_por_persona, name='detalle_picking_por_persona'),
    path('detalle_pend_pk/', detalle_pend_pk, name='detalle_pend_pk'),
    path('detalle_proc_arm/', detalle_proc_arm, name='detalle_proc_arm'),
    path('detalle_proc_pk/', detalle_proc_pk, name='detalle_proc_pk'),
    path('detalle_por_subcliente/<subcliente>/', detalle_por_subcliente, name='detalle_por_subcliente'),
    path('monitor/', monitor, name='monitor'),
    path('consulta_planilla/', consulta_planilla, name='consulta_planilla'),
    



]



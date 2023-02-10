from .models import GlobalPK
from datetime import datetime, date, timedelta

hoy = date.today()
un_dia = timedelta(1)
dos_dias = timedelta(2)
tres_dias = timedelta(3)


def tarjetas_preparacion_pedidos():
    
    pendiente_pk = GlobalPK.objects.filter(estado_picking = 'Pendiente')
    en_proceso_pk = GlobalPK.objects.filter(en_picking='Si')
    finalizado_pk = GlobalPK.objects.filter(estado_picking='Finalizado')
    finalizado_pk_hoy = finalizado_pk.filter(fecha_picking=hoy)
    
    pendiente_arm = GlobalPK.objects.filter(estado_armado = 'Pendiente')
    en_proceso_arm = GlobalPK.objects.filter(en_armado='Si')
    finalizado_arm = GlobalPK.objects.filter(estado_armado='Finalizado')
    finalizado_arm_hoy = finalizado_arm.filter(fecha_finalizado_armado=hoy)
    base_del_dia_hoy = GlobalPK.objects.filter(fecha_procesado=hoy)
    
    pendiente_pk_dia = 0
    finalizado_pk_dia = 0
    en_proceso_pk_dia = 0
    
    pendiente_arm_dia = 0
    finalizado_arm_dia = 0
    en_proceso_arm_dia = 0
    
    base_del_dia = 0
    
    for valor in pendiente_pk:
        pendiente_pk_dia += valor.unidades
    
    for valor in en_proceso_pk:
        en_proceso_pk_dia += valor.unidades
        
    for valor in finalizado_pk_hoy:
        finalizado_pk_dia += valor.unidades
        
        
        
    for valor in pendiente_arm:
        pendiente_arm_dia += valor.unidades
    
    for valor in en_proceso_arm:
        en_proceso_arm_dia += valor.unidades
        
    for valor in finalizado_arm_hoy:
        finalizado_arm_dia += valor.unidades
    
    for valor in base_del_dia_hoy:
        base_del_dia += valor.unidades
    
    
    
    
    return pendiente_pk_dia, finalizado_pk_dia, en_proceso_pk_dia, pendiente_arm_dia, finalizado_arm_dia, en_proceso_arm_dia, base_del_dia


ver_dato = tarjetas_preparacion_pedidos()

print(ver_dato)

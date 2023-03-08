#!/usr/bin/env python
# -*- coding: utf-8 -*-


from cgi import FieldStorage
from ..models import GlobalPK, Pendientes, PendientesArm
from datetime import datetime, date, timedelta
import calendar

formato_fecha2 = "%d/%m/%Y"

def actualizar_informe_global():
    
    hoy = datetime.today()
    dia = hoy.day
    mes = hoy.month
    anio = hoy.year
    
    validar_lunes = calendar.weekday(anio, mes, dia)
    
    
    delta1 = timedelta(1)
    delta2 = timedelta(2)
    delta3 = timedelta(3)
    delta4 = timedelta(4)
    delta5 = timedelta(5)
    
    
    
    if validar_lunes == 0:
        ayer = hoy - delta3
        antes_de_ayer = hoy - delta4
        anterior_a = hoy - delta5
    elif validar_lunes == 1:
        ayer = hoy - delta1
        antes_de_ayer = hoy - delta4
        anterior_a = hoy - delta5
    else:
        ayer = hoy - delta1
        antes_de_ayer = hoy -delta2
        anterior_a = hoy - delta3
        
    fecha_hoy = str(dia) + '/' + str(mes) + '/' + str(anio)
    fecha_hoy_f = datetime.strptime(fecha_hoy, formato_fecha2)
    
    todos_globales = GlobalPK.objects.all()
    pend_picking = todos_globales.filter(estado_picking='Pendiente')
    finalizados = todos_globales.filter(estado_picking='Finalizado')
    finalizado_hoy = finalizados.filter(fecha_picking=fecha_hoy_f)
    
    pend_armado = GlobalPK.objects.filter(estado_armado='Pendiente')
    finalizados_armado = GlobalPK.objects.filter(estado_armado='Finalizado')
    
    finalizado_armado_hoy = finalizados_armado.filter(fecha_armado=fecha_hoy_f)
    
    
    canales = Pendientes.objects.all()
    canales_arm = PendientesArm.objects.all()
    
    
    for valor in pend_armado:
        
        hoy_a = date.today()
        
        fecha_proceso = valor.fecha_procesado
        dia_proceso = fecha_proceso.day
        mes_proceso = fecha_proceso.month
        anio_proceso = fecha_proceso.year
        fecha_proceso_f = date(anio_proceso, mes_proceso, dia_proceso)
        
        dias_pend = (hoy_a - fecha_proceso_f).days
        
        
        filtro_canal_arm = canales_arm.filter(canal=valor.nombre_planilla)
        
        
        if not filtro_canal_arm:
            nuevo_pendiente_arm = PendientesArm(
                canal = valor.nombre_planilla
                
            )
            
            if dias_pend >= 3:
                nuevo_pendiente_arm.pend_tres_o_mas = valor.unidades
                nuevo_pendiente_arm.pend_dos = 0
                nuevo_pendiente_arm.pend_uno = 0
                nuevo_pendiente_arm.base_del_dia = 0
                nuevo_pendiente_arm.finalizado = 0
                nuevo_pendiente_arm.pendiente_para_sig_dia = valor.unidades
            elif dias_pend == 2:
                nuevo_pendiente_arm.pend_tres_o_mas = 0
                nuevo_pendiente_arm.pend_dos = valor.unidades
                nuevo_pendiente_arm.pend_uno = 0
                nuevo_pendiente_arm.base_del_dia = 0
                nuevo_pendiente_arm.finalizado = 0
                nuevo_pendiente_arm.pendiente_para_sig_dia = valor.unidades
            elif dias_pend == 1:
                nuevo_pendiente_arm.pend_tres_o_mas = 0
                nuevo_pendiente_arm.pend_dos = 0
                nuevo_pendiente_arm.pend_uno = valor.unidades
                nuevo_pendiente_arm.base_del_dia = 0
                nuevo_pendiente_arm.finalizado = 0
                nuevo_pendiente_arm.pendiente_para_sig_dia = valor.unidades
            else:
                nuevo_pendiente_arm.pend_tres_o_mas = 0
                nuevo_pendiente_arm.pend_dos = 0
                nuevo_pendiente_arm.pend_uno = 0
                nuevo_pendiente_arm.base_del_dia = valor.unidades
                nuevo_pendiente_arm.finalizado = 0
                nuevo_pendiente_arm.pendiente_para_sig_dia = valor.unidades
            
            nuevo_pendiente_arm.save()
                   
        
        
        else:
            canal_arm = PendientesArm.objects.get(canal=valor.nombre_planilla)
            
            if dias_pend >= 3:
                canal_arm.pend_tres_o_mas += valor.unidades
                canal_arm.pendiente_para_sig_dia += valor.unidades
                
            elif dias_pend == 2:
                canal_arm.pend_dos += valor.unidades
                canal_arm.pendiente_para_sig_dia += valor.unidades
                
            elif dias_pend == 1:
                canal_arm.pend_uno += valor.unidades
                canal_arm.pendiente_para_sig_dia += valor.unidades
                
            else:
                canal_arm.base_del_dia += valor.unidades
                canal_arm.pendiente_para_sig_dia += valor.unidades
                
            
            
            canal_arm.save()
            
    
    for finalizado_arm in finalizado_armado_hoy:
        
        if finalizado_arm:
            filtro = canales_arm.filter(canal=finalizado_arm.nombre_planilla)
            
            if filtro:
                
                filtro_arm = canales_arm.get(canal=finalizado_arm.nombre_planilla)
            
                filtro_arm.finalizado += finalizado_arm.unidades
                filtro_arm.save()
            
    
    
    informacion_arm = set(PendientesArm.objects.all())
    
    for valor in canales_arm:
        canal = canales_arm.get(canal=valor.canal)
        canal.canal = valor.canal
        canal.pend_tres_o_mas = 0
        canal.pend_dos = 0
        canal.pend_uno = 0
        canal.base_del_dia = 0
        canal.finalizado = 0
        canal.pendiente_para_sig_dia = 0
        canal.save()
        
        
        
    for valor in pend_picking:
        
        hoy_a = date.today()
        
        fecha_proceso = valor.fecha_procesado
        dia_proceso = fecha_proceso.day
        mes_proceso = fecha_proceso.month
        anio_proceso = fecha_proceso.year
        fecha_proceso_f = date(anio_proceso, mes_proceso, dia_proceso)
        
        dias_pend = (hoy_a - fecha_proceso_f).days
        #unidades, _ = GlobalPK.objects.get_or_create(nombre_planilla=valor.nombre_planilla)
        
        
        filtro_canal = canales.filter(canal=valor.nombre_planilla)
        
        
        if not filtro_canal:
            nuevo_pendiente = Pendientes(
                canal = valor.nombre_planilla
                
            )
            
            if dias_pend >= 3:
                nuevo_pendiente.pend_tres_o_mas = valor.unidades
                nuevo_pendiente.pend_dos = 0
                nuevo_pendiente.pend_uno = 0
                nuevo_pendiente.base_del_dia = 0
                nuevo_pendiente.finalizado = 0
                nuevo_pendiente.pendiente_para_sig_dia = valor.unidades
            elif dias_pend == 2:
                nuevo_pendiente.pend_tres_o_mas = 0
                nuevo_pendiente.pend_dos = valor.unidades
                nuevo_pendiente.pend_uno = 0
                nuevo_pendiente.base_del_dia = 0
                nuevo_pendiente.finalizado = 0
                nuevo_pendiente.pendiente_para_sig_dia = valor.unidades
            elif dias_pend == 1:
                nuevo_pendiente.pend_tres_o_mas = 0
                nuevo_pendiente.pend_dos = 0
                nuevo_pendiente.pend_uno = valor.unidades
                nuevo_pendiente.base_del_dia = 0
                nuevo_pendiente.finalizado = 0
                nuevo_pendiente.pendiente_para_sig_dia = valor.unidades
            else:
                nuevo_pendiente.pend_tres_o_mas = 0
                nuevo_pendiente.pend_dos = 0
                nuevo_pendiente.pend_uno = 0
                nuevo_pendiente.base_del_dia = valor.unidades
                nuevo_pendiente.finalizado = 0
                nuevo_pendiente.pendiente_para_sig_dia = valor.unidades
            
            nuevo_pendiente.save()
                   
        
        
        else:
            canal = Pendientes.objects.get(canal=valor.nombre_planilla)
            
            if dias_pend >= 3:
                canal.pend_tres_o_mas += valor.unidades
                canal.pendiente_para_sig_dia += valor.unidades
                
            elif dias_pend == 2:
                canal.pend_dos += valor.unidades
                canal.pendiente_para_sig_dia += valor.unidades
                
            elif dias_pend == 1:
                canal.pend_uno += valor.unidades
                canal.pendiente_para_sig_dia += valor.unidades
                
            else:
                canal.base_del_dia += valor.unidades
                canal.pendiente_para_sig_dia += valor.unidades
                
            
            
            canal.save()
            
    
    for finalizado in finalizado_hoy:
        
        if finalizado:
            filtro1 = canales.filter(canal=finalizado.nombre_planilla)
            if filtro1:
                filtro = canales.get(canal=finalizado.nombre_planilla)
            
                filtro.finalizado += finalizado.unidades
                filtro.save()
            
    
    
    informacion = set(Pendientes.objects.all())
    
    
    for valor in canales:
        canal = canales.get(canal=valor.canal)
        canal.canal = valor.canal
        canal.pend_tres_o_mas = 0
        canal.pend_dos = 0
        canal.pend_uno = 0
        canal.base_del_dia = 0
        canal.finalizado = 0
        canal.pendiente_para_sig_dia = 0
        canal.save()
        
    
    
    
    
    
    totales = GlobalPK.objects.filter(estado_picking='Pendiente')
    totales_arm = GlobalPK.objects.filter(estado_armado='Pendiente')
    hoy2 = date.today()
    cero = 0
    uno = 0
    dos = 0
    mas_de_tres = 0
    maniana = 0
    cero_arm = 0
    uno_arm = 0
    dos_arm = 0
    mas_de_tres_arm = 0
    maniana_arm = 0
    
    
    for valor in totales:
        if valor.fecha_procesado == hoy2:
            
            cero += valor.unidades
            
        elif valor.fecha_procesado == hoy2 - delta1:
            uno += valor.unidades
            
        elif valor.fecha_procesado == hoy2 -delta2:
            dos += valor.unidades
            
        elif valor.fecha_procesado <= hoy2 - delta3:
            mas_de_tres += valor.unidades
            
        if valor:
            maniana += valor.unidades
        
        
        
    for valor in totales_arm:
        

        
        if valor.fecha_procesado == hoy2:
            
            cero_arm += valor.unidades
            
        elif valor.fecha_procesado == hoy2 - delta1:
            uno_arm += valor.unidades
            
        elif valor.fecha_procesado == hoy2 -delta2:
            dos_arm += valor.unidades
            
        elif valor.fecha_procesado <= hoy2 - delta3:
            mas_de_tres_arm += valor.unidades
            
        if valor:
            maniana_arm += valor.unidades
        
    
    
    
    
    total_finalizado = GlobalPK.objects.filter(fecha_picking=hoy2)
    pk_fin = total_finalizado.filter(estado_picking='Finalizado')
    total_finalizado_arm = GlobalPK.objects.filter(fecha_finalizado_armado=hoy2)
    arm_fin = total_finalizado_arm.filter(estado_armado='Finalizado')
    
    fin_arm = 0
    for valor in arm_fin:
        
        fin_arm += valor.unidades
    
    fin_pk = 0
    for valor in pk_fin:
        
        fin_pk += valor.unidades
    
    
    return {'anterior_a':anterior_a,
            'antes_ayer':antes_de_ayer,
            'ayer':ayer,
            'hoy':fecha_hoy, 
            'informacion':informacion, 
            'informacion_arm':informacion_arm,
            
            'total_pk_3':mas_de_tres,
            'total_pk_2':dos,
            'total_pk_1':uno,
            'total_pk_0':cero,
            'total_pk_maniana':maniana,
            
            'total_arm_3':mas_de_tres_arm,
            'total_arm_2':dos_arm,
            'total_arm_1':uno_arm,
            'total_arm_0':cero_arm,
            'total_arm_maniana':maniana_arm,
            
            'fin_arm':fin_arm,
            'fin_pk':fin_pk
    }
            
    
    
    
    
    
    
    
if 'tablapk' in FieldStorage:
    print(actualizar_informe_global())
else:
    print("")
    
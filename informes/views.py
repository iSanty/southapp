from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormNuevoPK, FormSubCliente, FormPersonalDeposito, FormSector, FormFinalizarPK, FormFinalizarArm, FormIniciarPK, FormIniciarArm, FormEditarGlobal, FormNombrePlanilla, FormFiltroPlanilla
from .models import GlobalPK, SectorDepo, SubClientes, PersonalDeposito, Pendientes, PendientesArm, PendientePkPorDia, PenditenteArmPorDia, FinalizadoArmPorDia, FinalizadoPkPorDia, NombrePlanilla
from datetime import datetime, date, timedelta
import calendar



formato_fecha = "%d/%m/%Y %H:%M:%S"
formato_fecha2 = "%d/%m/%Y"
hoy = datetime.today()
dia = hoy.day
mes = hoy.month
anio = hoy.year
fecha_hoy = str(dia) + '/' + str(mes) + '/' + str(anio)
fecha_hoy_f = datetime.strptime(fecha_hoy, formato_fecha2)


def consulta_planilla(request):
    
    if request.method == 'POST':
        
        form = FormFiltroPlanilla(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            
            fecha_inicial = informacion['fecha_inicial']
            fecha_final = informacion['fecha_final']
            fecha_de = informacion['fecha_de']
            
            picking = informacion ['picking']
            
            estado_de = informacion['estado_de']
            
            cliente = informacion['cliente']
            operario = informacion['operario']
            
            if picking:
                tabla = GlobalPK.objects.filter(numero=picking)
                if tabla:
                    tabla = GlobalPK.objects.get(numero=picking)
                    msj = 'Resultado de la busqueda: '
                    return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj, 'tabla':tabla})
                else:
                    msj = 'Número de picking ' + str(picking) + ' inexistente.'
                    return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj})
            
            globales = GlobalPK.objects.all()
            tabla = []
            
            
            
            
            
            if fecha_de == 'Procesado' and estado_de == '1' and cliente == None and operario == None:
                for valor in globales:
                    if valor.fecha_procesado >= fecha_inicial and valor.fecha_procesado <= fecha_final:
                        tabla.append(valor)
                if not tabla:
                    msj = 'Sin resultados.'
                    return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj})
                msj = 'Resultado de la busqueda: '
                return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj, 'tabla':tabla})
                
                
            elif fecha_de == 'Pickeo' and estado_de == '1' and cliente == None and operario == None:
                for valor in globales:
                    if valor.fecha_inicio_picking >= fecha_inicial and valor.fecha_inicio_picking <= fecha_final: 
                        tabla.append(valor)
                if not tabla:
                    msj = 'Sin resultados.'
                    return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj})
                msj = 'Resultado de la busqueda: '
                return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj, 'tabla':tabla})
            
            
            elif fecha_de == 'Armado' and estado_de == '1' and cliente == None and operario == None:
                for valor in globales:
                    if valor.fecha_armado >= fecha_inicial and valor.fecha_armado <= fecha_final:                            
                        tabla.append(valor)
                if not tabla:
                    msj = 'Sin resultados.'
                    return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj})
                msj = 'Resultado de la busqueda: '
                return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj, 'tabla':tabla})
            
            
            elif fecha_de == 'Fin Pickeo' and estado_de == '1' and cliente == None and operario == None:
                for valor in globales:
                    if valor.fecha_picking >= fecha_inicial and valor.fecha_picking <= fecha_final:                            
                        tabla.append(valor)
                if not tabla:
                    msj = 'Sin resultados.'
                    return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj})
                msj = 'Resultado de la busqueda: '
                return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj, 'tabla':tabla})
                        
                        
            elif fecha_de == 'Fin Armado' and estado_de == '1' and cliente == None and operario == None:
                for valor in globales:
                    if valor.fecha_finalizado_armado >= fecha_inicial and valor.fecha_finalizado_armado <= fecha_final:                            
                        tabla.append(valor)
                if not tabla:
                    msj = 'Sin resultados.'
                    return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj})
                msj = 'Resultado de la busqueda: '
                return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj, 'tabla':tabla})
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            else:
                msj = 'Sin resultados.'
                return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj})
        
        
        else:
            msj = 'Formulario inválido, reintente.'
            return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj})
            
    else:
        fecha_inicio = date(2022, 8, 1) #fecha inicio de desarrollo
        fecha_inicio_f = str(fecha_inicio.day) + '/' + str(fecha_inicio.month) + '/' + str(fecha_inicio.year)
        form = FormFiltroPlanilla(initial={
            'fecha_inicial':fecha_inicio_f,
            'fecha_final':fecha_hoy,
            
            })
        
        msj = 'Llene 1 o más campos para buscar'
        return render(request, 'informes/consulta_planilla.html', {'form':form,'msj':msj})
            
            


def monitor(request):
    detalle = 0
    return render(request, 'informes/monitor.html',{'detalle':detalle})


def detalle_por_subcliente(request, subcliente):
    detalle_sub = GlobalPK.objects.filter(nombre_planilla=subcliente)
    detalle = detalle_sub.filter(estado_armado='Pendiente')
    return render(request, 'informes/detalle_por_subcliente.html',{'detalle':detalle})



def detalle_pend_pk(request):
    detalle = GlobalPK.objects.filter(estado_picking='Pendiente')
    
    return render(request, 'informes/detalle_pend_pk.html',{'detalle':detalle})
    
    
    

def detalle_proc_pk(request):
    detalle = GlobalPK.objects.filter(en_picking='Si')
    
    return render(request, 'informes/detalle_proc_pk.html',{'detalle':detalle})


def detalle_fin_pk(request):
    detalle2 = GlobalPK.objects.filter(estado_picking='Finalizado')
    detalle = detalle2.filter(fecha_procesado=fecha_hoy_f)
    
    return render(request, 'informes/detalle_fin_pk.html',{'detalle':detalle})

def detalle_pend_arm(request):
    detalle = GlobalPK.objects.filter(estado_armado='Pendiente')
    
    return render(request, 'informes/detalle_pend_arm.html',{'detalle':detalle})

def detalle_proc_arm(request):
    detalle = GlobalPK.objects.filter(en_armado='Si')
    
    return render(request, 'informes/detalle_proc_arm.html',{'detalle':detalle})

def detalle_fin_arm(request):
    detalle2 = GlobalPK.objects.filter(estado_armado='Finalizado')
    detalle = detalle2.filter(fecha_procesado=fecha_hoy_f)
    
    return render(request, 'informes/detalle_fin_pk.html',{'detalle':detalle})

def detalle_base_dia(request):
    detalle = GlobalPK.objects.filter(fecha_procesado=fecha_hoy_f)
    
    return render(request, 'informes/detalle_base_dia.html',{'detalle':detalle})





@login_required
def inciar_picking(request):
    user = request.user
    form = FormIniciarPK(initial={
            'fecha_inicio_picking':hoy.strftime(formato_fecha2),
            'hora':datetime.now().time()
        })
    pendientes_pk = GlobalPK.objects.filter(en_picking='No')
    if request.method == 'POST':
        form = FormIniciarPK(request.POST)
        
        
        
        if form.is_valid():
            informacion = form.cleaned_data
            picking_en_base = GlobalPK.objects.filter(numero=informacion['numero'])
            if not picking_en_base:
                msj = 'Nro de global inexistente'
                return render(request, 'informes/iniciar_picking.html',{'msj_error':msj, 'form':form,'pendientes_pk':pendientes_pk})

            picking_en_base = GlobalPK.objects.get(numero=informacion['numero'])
            if picking_en_base.en_armado == 'Si' or picking_en_base.en_picking == 'Si':
                if picking_en_base.en_armado == 'Si':
                    msj = 'El global se encuentra en proceso de Armado, verifique.'
                    return render(request, 'informes/iniciar_picking.html',{'msj_error':msj, 'form':form,'pendientes_pk':pendientes_pk})
                elif picking_en_base.en_picking == 'Si':
                    msj = 'El global ya se encuentra iniciado.'
                    return render(request, 'informes/iniciar_picking.html',{'msj_error':msj, 'form':form,'pendientes_pk':pendientes_pk})
            
            if picking_en_base.estado_armado == 'Finalizado' or picking_en_base.estado_picking == 'Finalizado':
                if picking_en_base.estado_picking == 'Finalizado':
                    msj = 'El global se encuentra en estado de PK Finalizado.'
                    return render(request, 'informes/iniciar_picking.html',{'msj_error':msj, 'form':form,'pendientes_pk':pendientes_pk})
                elif picking_en_base.estado_armado == 'Finalizado':
                    msj = 'El global se encuentra en estado de ARM Finalizado.'
                    return render(request, 'informes/iniciar_picking.html',{'msj_error':msj, 'form':form,'pendientes_pk':pendientes_pk})
                
                
            picking_en_base.en_picking = 'Si'
            picking_en_base.fecha_inicio_picking = informacion['fecha_inicio_picking']
            
            
            picking_en_base.hora_inicio_picking = informacion['hora']
            picking_en_base.iniciado_por = str(informacion['iniciado_por'])
            picking_en_base.usuario_inicio = str(user)
            picking_en_base.save()
            
            msj = 'Picking iniciado correctamente'
            return render(request, 'informes/iniciar_picking.html',{'form':form, 'msj_ok':msj, 'pendientes_pk':pendientes_pk})
        else:
            msj = 'Formulario inválido'
            return render(request, 'informes/iniciar_picking.html',{'form':form, 'msj_error':msj, 'pendientes_pk':pendientes_pk})

    else:
        
        
        msj = 'Escriba o seleccione un numero para iniciar.'
        return render(request, 'informes/iniciar_picking.html',{'form':form, 'msj_inicio':msj, 'pendientes_pk':pendientes_pk})






@login_required
def iniciar_armado(request):
    user = request.user
    form = FormIniciarArm(initial={
        'fecha_armado':hoy.strftime(formato_fecha2),
        'hora':datetime.now().time()
    })
    pendientes_arm = GlobalPK.objects.filter(en_armado='No')
    if request.method == 'POST':
        form = FormIniciarArm(request.POST)
        
        
        
        if form.is_valid():
            informacion = form.cleaned_data
            picking_en_base = GlobalPK.objects.filter(numero=informacion['numero'])
            if not picking_en_base:
                msj = 'Nro de global inexistente'
                return render(request, 'informes/iniciar_armado.html',{'msj_error':msj, 'form':form,'pendientes_arm':pendientes_arm})

            picking_en_base = GlobalPK.objects.get(numero=informacion['numero'])
            if picking_en_base.en_armado == 'Si' or picking_en_base.en_picking == 'Si':
                if picking_en_base.en_armado == 'Si':
                    msj = 'El global se encuentra en proceso de Armado, verifique.'
                    return render(request, 'informes/iniciar_armado.html',{'msj_error':msj, 'form':form,'pendientes_arm':pendientes_arm})
                elif picking_en_base.en_picking == 'Si':
                    msj = 'No ha sido cerrado el global en la instancia de picking.'
                    return render(request, 'informes/iniciar_armado.html',{'msj_error':msj, 'form':form,'pendientes_arm':pendientes_arm})
            
            if picking_en_base.estado_armado == 'Finalizado':
                if picking_en_base.estado_armado == 'Finalizado':
                    msj = 'El global se encuentra en estado de ARM Finalizado.'
                    return render(request, 'informes/iniciar_armado.html',{'msj_error':msj, 'form':form,'pendientes_arm':pendientes_arm})
                
                
            picking_en_base.en_armado = 'Si'
            picking_en_base.fecha_armado = informacion['fecha_armado']
            
            picking_en_base.hora_inicio_armado = informacion['hora']
            picking_en_base.inicio_arm_por = str(informacion['inicio_arm_por'])
            picking_en_base.usuario_inicio_arm = str(user)
            picking_en_base.save()
            
            msj = 'Armado iniciado correctamente'
            
            return render(request, 'informes/iniciar_armado.html',{'msj_ok':msj, 'form':form,'pendientes_arm':pendientes_arm})
        else:
            msj = 'Formulario inválido'
            return render(request, 'informes/iniciar_picking.html',{'form':form, 'msj_error':msj, 'pendientes_arm':pendientes_arm})
    
    else:
        
        
        msj = 'Escriba o seleccione un numero para iniciar.'
        return render(request, 'informes/iniciar_armado.html',{'form':form, 'msj_inicio':msj, 'pendientes_arm':pendientes_arm})
        






@login_required
def finalizar_armado(request):
    user = request.user
    form = FormFinalizarArm(initial={
        'fecha_finalizado_armado':hoy.strftime(formato_fecha2),
        'hora_fin_armado':datetime.now().time()
    })
    
    if request.method == 'POST':
        form = FormFinalizarArm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            
            pk_finalizado_a = GlobalPK.objects.all()
            pk_finalizado = pk_finalizado_a.filter(numero=informacion['numero'])
            if not pk_finalizado:
                msj = 'Nro de global inexistente'
                return render(request, 'informes/finalizar_armado.html', {'msj_error':msj, 'form':form})
            
            
            pk_finalizado_b = GlobalPK.objects.get(numero=informacion['numero'])
            if pk_finalizado_b.estado_picking == 'Pendiente':
                msj = 'El global nro ' + str(informacion['numero']) + ' no se encuentra con el picking finalizado'
                return render(request, 'informes/finalizar_armado.html', {'msj_error':msj, 'form':form})
            
            
            
            pk_finalizado_b.estado_armado = 'Finalizado'
            
            pk_finalizado_b.en_armado = 'Terminado'
            
            pk_finalizado_b.fecha_finalizado_armado = informacion['fecha_finalizado_armado']
            pk_finalizado_b.finalizado_arm_por = str(user)
            pk_finalizado_b.hora_inicio_armado = informacion['hora_inicio_armado']
            pk_finalizado_b.hora_fin_armado = informacion['hora_fin_armado']
            pk_finalizado_b.contribuyentes = informacion['contribuyentes']
            
            pk_finalizado_b.save()
            
            
            
            
            msj = 'Globlal ' + str(informacion['numero']) + ': Armado finalizado.'
            return render(request, 'informes/finalizar_armado.html', {'msj_ok':msj, 'form':form})
                
        msj = 'Formulario inválido'
        return render(request, 'informes/finalizar_armado.html', {'msj_error':msj, 'form':form})
    msj = 'Ingrese un numero de global de picking'
    return render(request, 'informes/finalizar_armado.html', {'msj_inicio':msj, 'form':form})


@login_required
def finalizar_global(request):
    user = request.user
    form = FormFinalizarPK(initial={'fecha_picking':hoy.strftime(formato_fecha2),
                                    'hora_fin_pk':datetime.now().time()})
    if request.method == 'POST':
        
        form = FormFinalizarPK(request.POST)
        
        if form.is_valid():
            informacion = form.cleaned_data
            global_en_base_b = GlobalPK.objects.all()
            global_en_base = global_en_base_b.filter(numero=informacion['numero'])
            
            if not global_en_base:
                msj = 'No existe el numero de global ' + str(informacion['numero'])
                return render(request, 'informes/finalizar_global.html',{'form':form, 'msj_error':msj})
            
            
            global_en_base_a = GlobalPK.objects.get(numero=informacion['numero'])
            
            if global_en_base_a.estado_picking == 'Finalizado':
                msj = 'El numero de global ya se encuentra finalizado por el usuario ' + global_en_base_a.finalizado_pk_por + ' el día ' + str(global_en_base_a.fecha_picking)
                return render(request, 'informes/finalizar_global.html',{'msj_error':msj, 'form':form})
                
            global_en_base_a.estado_picking = 'Finalizado'
            global_en_base_a.en_picking = 'Terminado'
            global_en_base_a.operario = str(informacion['operario'])
            global_en_base_a.fecha_picking = informacion['fecha_picking']
            global_en_base_a.hora_inicio_picking = informacion['hora_inicio_pk']
            global_en_base_a.hora_fin_picking = informacion['hora_fin_pk'] #datetime.now().time()
            global_en_base_a.finalizado_pk_por = str(user)
            
            global_en_base_a.save()
            
            
            msj = 'Global numero ' + str(informacion['numero']) + ' finalizado correctamente'
            return render(request, 'informes/finalizar_global.html',{'msj_ok':msj, 'form':form})
        else:
            form = FormFinalizarPK(request.POST)
            msj = 'Formulario invalido'
            return render(request, 'informes/finalizar_global.html',{'msj_error':msj, 'form':form})
        
    msj = 'Llene los datos solicitados. Para editar, finalizar con nuevos datos'
    return render(request, 'informes/finalizar_global.html',{'msj_inicio':msj, 'form':form})



@login_required
def index_informes_2(request):
    
    
    pendiente_pk = GlobalPK.objects.filter(estado_picking = 'Pendiente')
    en_proceso_pk = GlobalPK.objects.filter(en_picking='Si')
    finalizado_pk = GlobalPK.objects.filter(estado_picking='Finalizado')
    finalizado_pk_hoy = finalizado_pk.filter(fecha_picking=fecha_hoy_f)
    
    pendiente_arm = GlobalPK.objects.filter(estado_armado = 'Pendiente')
    en_proceso_arm = GlobalPK.objects.filter(en_armado='Si')
    finalizado_arm = GlobalPK.objects.filter(estado_armado='Finalizado')
    finalizado_arm_hoy = finalizado_arm.filter(fecha_finalizado_armado=fecha_hoy_f)
    base_del_dia_hoy = GlobalPK.objects.filter(fecha_procesado=fecha_hoy_f)
    
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
        
        
        
    #calculo piking por hora
    total_pickeado = finalizado_pk_dia
    
    
            
    
    return render(request, 'informes/index_informes2.html', {'pendiente_pk_dia':pendiente_pk_dia,
                                                             'en_proceso_pk_dia':en_proceso_pk_dia,
                                                             'finalizado_pk_dia':finalizado_pk_dia,
                                                             'pendiente_arm_dia':pendiente_arm_dia,
                                                             'en_proceso_arm_dia':en_proceso_arm_dia,
                                                             'finalizado_arm_dia':finalizado_arm_dia,
                                                             'base_del_dia':base_del_dia
                                                             
                                                             
                                                             
                                                             })


@login_required
def index_informes(request):
    
    informacion_pk_pend = GlobalPK.objects.filter(estado_picking='Pendiente').order_by('-numero')
    informacion_arm_pend = GlobalPK.objects.filter(estado_armado='Pendiente').order_by('-numero')
    
    informacion_pk_finalizado = GlobalPK.objects.filter(estado_picking='Finalizado')
    informacion_arm_finalizado = GlobalPK.objects.filter(estado_picking='Finalizado')
    
    hoy = datetime.today()
    dia = hoy.day
    mes = hoy.month
    anio = hoy.year
    fecha_hoy = str(dia) + '/' + str(mes) + '/' + str(anio)
    fecha_hoy_f = datetime.strptime(fecha_hoy, formato_fecha2)
    
    
    inf_pk_fin = informacion_pk_finalizado.filter(fecha_picking=fecha_hoy_f).order_by('-numero')
    inf_arm_fin = informacion_arm_finalizado.filter(fecha_armado=fecha_hoy_f).order_by('-numero')
    
    
    
    return render(request, 'informes/index_informes.html', {'informacion_pk_pend':informacion_pk_pend, 'informacion_arm_pend':informacion_arm_pend, 'inf_pk_fin':inf_pk_fin, 'inf_arm_fin':inf_arm_fin})


def nuevo_global(request):
    user = request.user
    if request.method == 'POST':
        form = FormNuevoPK(request.POST)

        if form.is_valid():
            
            
            informacion = form.cleaned_data
            validar_global = informacion['numero']
            
            global_en_base = GlobalPK.objects.filter(numero=validar_global)
            
            if not global_en_base:
                picking = GlobalPK(
                    numero = informacion['numero'],
                    tipo = informacion['tipo'],
                    unidades = informacion['unidades'],
                    fecha_procesado = informacion['fecha_procesado'],
                    hora_procesado = informacion['hora_procesado'],
                    estado_picking = 'Pendiente',
                    estado_armado = 'Pendiente',
                    creado_por = user,
                    fecha_creacion = fecha_hoy_f,
                    nombre_planilla = informacion['nombre_planilla'],
                    en_picking = 'No',
                    en_armado = 'No',

                )

                picking.save()
                
                
                
                global_grabado_b = GlobalPK.objects.all()
                
                global_grabado = global_grabado_b.filter(estado_picking='Pendiente').order_by('-id')
                
                msj = 'Global ' + str(informacion['numero']) + ' creado exitosamente'
                return render(request, 'informes/nuevo_global.html',{'form':form, 'msj_ok':msj,'global_grabado':global_grabado})
            else:
                msj = 'El numero' + str(informacion['numero']) + ' ya existe en la base de datos'
                return render(request, 'informes/nuevo_global.html',{'form':form, 'msj_error':msj})
            
        msj = 'Formulario inválido'
        return render(request, 'informes/nuevo_global.html',{'form':form, 'msj_error':msj})
    
    else:
        form = FormNuevoPK(initial={
            'fecha_procesado':hoy.strftime(formato_fecha2)
        })
        msj = 'Llene los campos solicitados'
    
        return render(request, 'informes/nuevo_global.html',{'form':form, 'msj_inicio':msj})



@login_required
def informe_global(request):
       
    
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
    
    
    return render(request, 'informes/informe_global.html',{'anterior_a':anterior_a,
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
                                                           })

@login_required
def parametros(request):
    form_sub_cliente = FormNombrePlanilla()
    form_personal_deposito = FormPersonalDeposito()
    form_sector = FormSector()
    
    if request.method == 'POST':
        if 'btn_sub_cliente' in request.POST:
            form_sub_cliente = FormNombrePlanilla(request.POST)
            if form_sub_cliente.is_valid():
                informacion = form_sub_cliente.cleaned_data
                sub_en_base = NombrePlanilla.objects.filter(nombre=informacion['nombre'])
                if sub_en_base:
                    msj = 'El canal de descuento ' + informacion['nombre'] + ' ya se encuentra dado de alta.'
                    return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 
                                                                              'form_personal_deposito':form_personal_deposito, 
                                                                              'form_sector':form_sector, 
                                                                              'msj':msj})    

                sub_cliente = NombrePlanilla(
                    nombre = informacion['nombre'],
                    
                    
                )
                sub_cliente.save()
                msj = 'Canal ' + informacion['nombre'] + ' creado exitosamente'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 
                                                                          'form_personal_deposito':form_personal_deposito, 
                                                                          'form_sector':form_sector, 
                                                                          'msj':msj})    
            else:
                msj = 'Formulario inválido'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 
                                                                          'form_personal_deposito':form_personal_deposito, 
                                                                          'form_sector':form_sector, 
                                                                          'msj':msj})


        elif 'btn_sector' in request.POST:
            form_sector = FormSector(request.POST)
            if form_sector.is_valid():
                informacion = form_sector.cleaned_data
                sector_en_base = SectorDepo.objects.filter(descripcion=informacion['descripcion'])
                if sector_en_base:
                    msj = 'El sector ' + informacion['descripcion'] + ' ya se encuentra dado de alta.'
                    return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 
                                                                              'form_personal_deposito':form_personal_deposito, 
                                                                              'form_sector':form_sector, 
                                                                              'msj':msj})    

                sector = SectorDepo(
                    descripcion = informacion['descripcion']
                    
                )
                sector.save()
                msj = 'Sector ' + informacion['descripcion'] + ' creado exitosamente'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 
                                                                          'form_personal_deposito':form_personal_deposito, 
                                                                          'form_sector':form_sector, 
                                                                          'msj':msj})    
            else:
                msj = 'Formulario inválido'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 
                                                                          'form_personal_deposito':form_personal_deposito, 
                                                                          'form_sector':form_sector, 
                                                                          'msj':msj})    
        
        elif 'btn_personal_deposito' in request.POST:
            form_personal_deposito = FormPersonalDeposito(request.POST)
            if form_personal_deposito.is_valid():
                informacion = form_personal_deposito.cleaned_data
                personal_en_base = PersonalDeposito.objects.filter(dni=informacion['dni'])
                if personal_en_base:
                    msj = 'El empleado ' + informacion['nombre'] + ' ' + informacion['apellido'] +' con dni' + str(informacion['dni']) + ' ya se encuentra dado de alta.'
                    return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 
                                                                              'form_personal_deposito':form_personal_deposito, 
                                                                              'form_sector':form_sector, 
                                                                              'msj':msj})    

                empleado = PersonalDeposito(
                    dni = informacion['dni'],
                    nombre = informacion['nombre'],
                    apellido = informacion['apellido'],
                    sector = informacion['sector'],
                    
                )
                empleado.save()
                msj = 'Empleado con dni ' + str(informacion['dni']) + ' creado exitosamente'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 
                                                                          'form_personal_deposito':form_personal_deposito, 
                                                                          'form_sector':form_sector, 
                                                                          'msj':msj})    
            else:
                msj = 'Formulario inválido'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 
                                                                          'form_personal_deposito':form_personal_deposito, 
                                                                          'form_sector':form_sector, 
                                                                          'msj':msj})    
        
    
    
    
    msj = 'Ingrese los datos solicitados'
    return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 
                                                              'form_personal_deposito':form_personal_deposito, 
                                                              'form_sector':form_sector, 
                                                              'msj':msj})



def editar_global(request, id):
    user = request.user
    global_pk = GlobalPK.objects.get(id=id)
    form = FormEditarGlobal(initial={
        'numero':global_pk.numero,
        'cliente':global_pk.cliente,
        'sub_cliente':global_pk.sub_cliente,
        'unidades':global_pk.unidades,
        'fecha_procesado':global_pk.fecha_procesado,
        'hora_procesado':global_pk.hora_procesado,
        'fecha_creacion':global_pk.fecha_creacion,
        'fecha_procesado':global_pk.fecha_procesado,
        'hora_procesado':global_pk.fecha_procesado,
        'operario':global_pk.operario,
        'fecha_picking':global_pk.fecha_picking,
        'fecha_inicio_picking':global_pk.fecha_inicio_picking,
        'hora_inicio_picking':global_pk.hora_inicio_picking,
        'iniciado_por':global_pk.iniciado_por,
        'hora_fin_picking':global_pk.finalizado_pk_por,
        'usuario_inicio':global_pk.finalizado_pk_por,
        'fecha_armado':global_pk.fecha_armado,
        'fecha_finalizado_armado':global_pk.fecha_finalizado_armado,
        'hora_fin_armado':global_pk.hora_fin_armado,
        'hora_inicio_armado':global_pk.hora_inicio_armado,
        'inicio_arm_por':global_pk.inicio_arm_por,
        'inicio_arm_por':global_pk.inicio_arm_por,
        'finalizado_arm_por':global_pk.finalizado_arm_por,
        'usuario_inicio_arm':global_pk.usuario_inicio_arm,
        'estado_picking':global_pk.estado_picking,
        'estado_armado':global_pk.estado_armado,
        'en_picking':global_pk.en_picking,
        'en_armado':global_pk.en_armado
        
        
    })
    
    if request.method == 'POST':
        form = FormEditarGlobal(request.POST)
        if form.is_valid():
        
            global_pk.numero = form.cleaned_data.get('numero')
            global_pk.cliente = form.cleaned_data.get('cliente')
            global_pk.sub_cliente = form.cleaned_data.get('sub_cliente')
            global_pk.tipo = form.cleaned_data.get('tipo')
            global_pk.unidades = form.cleaned_data.get('unidades')
            global_pk.fecha_creacion = form.cleaned_data.get('fecha_creacion')
            global_pk.fecha_procesado = form.cleaned_data.get('fecha_procesado')
            global_pk.hora_procesado = form.cleaned_data.get('hora_procesado')
            global_pk.operario = form.cleaned_data.get('operario')
            
            
            global_pk.fecha_picking = form.cleaned_data.get('fecha_picking')
            global_pk.fecha_inicio_picking = form.cleaned_data.get('fecha_inicio_picking')
            global_pk.hora_inicio_picking = form.cleaned_data.get('hora_inicio_picking')
            global_pk.iniciado_por = form.cleaned_data.get('iniciado_por')
            global_pk.hora_fin_picking = form.cleaned_data.get('hora_fin_picking')
            global_pk.usuario_inicio = form.cleaned_data.get('usuario_inicio')
            global_pk.finalizado_pk_por = form.cleaned_data.get('finalizado_pk_por')
            global_pk.fecha_armado = form.cleaned_data.get('fecha_armado')
            global_pk.fecha_finalizado_armado = form.cleaned_data.get('fecha_finalizado_armado')
            global_pk.hora_fin_armado = form.cleaned_data.get('hora_fin_armado')
            
            global_pk.hora_inicio_armado = form.cleaned_data.get('hora_inicio_armado')
            global_pk.inicio_arm_por = form.cleaned_data.get('inicio_arm_por')
            global_pk.contribuyentes = form.cleaned_data.get('contribuyentes')
            global_pk.finalizado_arm_por = form.cleaned_data.get('finalizado_arm_por')
            global_pk.usuario_inicio_arm = form.cleaned_data.get('usuario_inicio_arm')
            
            global_pk.estado_picking = form.cleaned_data.get('estado_picking')
            global_pk.estado_armado = form.cleaned_data.get('estado_armado')
            global_pk.en_picking = form.en_picking.get('usuario_inicio_arm')
            global_pk.en_armado = form.en_armado.get('usuario_inicio_arm')
            
            
            global_pk.editado_por = user
            global_pk.fecha_edicion = fecha_hoy_f
            cantidad_antes = global_pk.cantidad_ediciones
            cantidad_antes += 1
            
            global_pk.cantidad_ediciones = cantidad_antes          
            
            
            global_pk.nombre_planilla = str(form.cleaned_data.get('cliente'))+'('+str(form.cleaned_data.get('sub_cliente'))+')'
            global_pk.save()
            msj = 'Global editado correctamente'
            return redirect('index_informes2')
        
        else:
            msj = 'Formulario inválido'
            return render(request, 'informes/editar_global.html',{'form':form, 'msj':msj, 'global':global_pk})
    else:
        msj = 'Edite según corresponda'
        return render(request, 'informes/editar_global.html', {'form':form, 'msj':msj, 'global':global_pk})
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FormNuevoPK, FormSubCliente, FormPersonalDeposito, FormSector, FormFinalizarPK, FormFinalizarArm
from .models import GlobalPK, SectorDepo, SubClientes, PersonalDeposito, Pendientes, PendientesArm
from datetime import datetime, date
import calendar



formato_fecha = "%d/%m/%Y %H:%M:%S"
formato_fecha2 = "%d/%m/%Y"
hoy = datetime.today()




@login_required
def finalizar_armado(request):
    form = FormFinalizarArm()
    
    if request.method == 'POST':
        form = FormFinalizarArm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            
            pk_finalizado_a = GlobalPK.objects.all()
            pk_finalizado = pk_finalizado_a.filter(numero=informacion['numero'])
            if not pk_finalizado:
                msj = 'Nro de global inexistente'
                return render(request, 'informes/finalizar_armado.html', {'msj':msj, 'form':form})
            
            pk_finalizado_b = GlobalPK.objects.get(numero=informacion['numero'])
            if pk_finalizado_b.estado_picking == 'Pendiente':
                msj = 'El global nro ' + str(informacion['numero']) + ' no se encuentra con el picking finalizado'
                return render(request, 'informes/finalizar_armado.html', {'msj':msj, 'form':form})
            
            
                
            pk_finalizado_b.estado_armado = 'Finalizado'
            
            pk_finalizado_b.fecha_armado = informacion['fecha_armado']
            
            if informacion['hora_fin_armado']:
                pk_finalizado_b.hora_fin_armado = informacion['hora_fin_armado']
            else:
                pk_finalizado_b.hora_fin_armado = '00:00:00'
                
            
            pk_finalizado_b.save()
            msj = 'Globlal ' + str(informacion['numero']) + ': Armado finalizado.'
            return render(request, 'informes/finalizar_armado.html', {'msj':msj, 'form':form})
                
        msj = 'Formulario inválido'
        return render(request, 'informes/finalizar_armado.html', {'msj':msj, 'form':form})
    msj = 'Ingrese un numero de global de picking'
    return render(request, 'informes/finalizar_armado.html', {'msj':msj, 'form':form})


@login_required
def finalizar_global(request):
    
    form = FormFinalizarPK()
    if request.method == 'POST':
        
        form = FormFinalizarPK(request.POST)
        
        if form.is_valid():
            informacion = form.cleaned_data
            global_en_base_b = GlobalPK.objects.all()
            global_en_base = global_en_base_b.filter(numero=informacion['numero'])
            
            if not global_en_base:
                msj = 'No existe el numero de global ' + str(informacion['numero'])
                return render(request, 'informes/finalizar_global.html',{'form':form, 'msj':msj})
            
            
            global_en_base_a = GlobalPK.objects.get(numero=informacion['numero'])
            global_en_base_a.estado_picking = 'Finalizado'
            global_en_base_a.operario = str(informacion['operario'])
            global_en_base_a.fecha_picking = informacion['fecha_picking']
            global_en_base_a.hora_inicio_picking = informacion['hora_inicio_picking']
            global_en_base_a.hora_fin_picking = informacion['hora_fin_picking']
            
            global_en_base_a.save()
            msj = 'Global numero ' + str(informacion['numero']) + ' finalizado correctamente'
            return render(request, 'informes/finalizar_global.html',{'msj':msj, 'form':form})
        else:
            form = FormFinalizarPK(request.POST)
            msj = 'Formulario invalido'
            return render(request, 'informes/finalizar_global.html',{'msj':msj, 'form':form})
        
    msj = 'Llene los datos solicitados. Para editar, finalizar con nuevos datos'
    return render(request, 'informes/finalizar_global.html',{'msj':msj, 'form':form})



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
    
    if request.method == 'POST':
        form = FormNuevoPK(request.POST)

        if form.is_valid():
            
            
            informacion = form.cleaned_data
            validar_global = informacion['numero']
            
            global_en_base = GlobalPK.objects.filter(numero=validar_global)
            
            if not global_en_base:
                picking = GlobalPK(
                    numero = informacion['numero'],
                    cliente = informacion['cliente'],
                    sub_cliente = informacion['sub_cliente'],
                    unidades = informacion['unidades'],
                    fecha_procesado = informacion['fecha_procesado'],
                    hora_procesado = informacion['hora_procesado'],
                    # operario = '',
                    # fecha_picking = '',
                    # hora_inicio_picking = informacion['hora_inicio_picking'],
                    # hora_fin_picking = informacion['hora_fin_picking'],
                    estado_picking = 'Pendiente',
                    estado_armado = 'Pendiente',
                    nombre_planilla = str(informacion['cliente'])+'('+str(informacion['sub_cliente'])+')'
                    # fecha_armado = '',
                    # hora_fin_armado = '',
                    
                )

                picking.save()
                global_grabado_b = GlobalPK.objects.all()
                
                global_grabado = global_grabado_b.filter(estado_picking='Pendiente').order_by('-id')
                
                msj = 'Global ' + str(informacion['numero']) + ' creado exitosamente'
                return render(request, 'informes/nuevo_global.html',{'form':form, 'msj':msj,'global_grabado':global_grabado})
            else:
                msj = 'El numero' + str(informacion['numero']) + ' ya existe en la base de datos'
                return render(request, 'informes/nuevo_global.html',{'form':form, 'msj':msj})
            
        msj = 'Formulario inválido'
        return render(request, 'informes/nuevo_global.html',{'form':form, 'msj':msj})
    
    else:
        form = FormNuevoPK()
        msj = 'Llene los campos solicitados'
    
        return render(request, 'informes/nuevo_global.html',{'form':form, 'msj':msj})



@login_required
def informe_global(request):
       
    
    hoy = datetime.today()
    dia = hoy.day
    mes = hoy.month
    anio = hoy.year
    validar_lunes = calendar.weekday(anio, mes, dia)
    
    
    if validar_lunes == 0:
        ayer = dia -3
        antes_de_ayer = dia -4
        anterior_a = dia - 5
    elif validar_lunes == 1:
        ayer = dia -1
        antes_de_ayer = dia -4
        anterior_a = dia - 5
    else:
        ayer = dia -1
        antes_de_ayer = dia -2
        anterior_a = dia - 3
        
    fecha_hoy = str(dia) + '/' + str(mes) + '/' + str(anio)
    fecha_ayer = str(ayer) + '/' + str(mes) + '/' + str(anio)
    fecha_antes_ayer = str(antes_de_ayer) + '/' + str(mes) + '/' + str(anio)
    fecha_anterior = str(anterior_a) + '/' + str(mes) + '/' + str(anio)
    fecha_hoy_f = datetime.strptime(fecha_hoy, formato_fecha2)
    # fecha_ayer_f = datetime.strptime(fecha_ayer, formato_fecha2)
    # fecha_antes_ayer_f = datetime.strptime(fecha_antes_ayer, formato_fecha2)
    # fecha_anterior_f = datetime.strptime(fecha_anterior, formato_fecha2)
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
        
        hoy = date.today()
        
        fecha_proceso = valor.fecha_procesado
        dia_proceso = fecha_proceso.day
        mes_proceso = fecha_proceso.month
        anio_proceso = fecha_proceso.year
        fecha_proceso_f = date(anio_proceso, mes_proceso, dia_proceso)
        
        dias_pend = (hoy - fecha_proceso_f).days
        
        
        
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
        
        hoy = date.today()
        
        fecha_proceso = valor.fecha_procesado
        dia_proceso = fecha_proceso.day
        mes_proceso = fecha_proceso.month
        anio_proceso = fecha_proceso.year
        fecha_proceso_f = date(anio_proceso, mes_proceso, dia_proceso)
        
        dias_pend = (hoy - fecha_proceso_f).days
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
        
    
    return render(request, 'informes/informe_global.html',{'anterior_a':fecha_anterior,'antes_ayer':fecha_antes_ayer,'ayer':fecha_ayer,'hoy':fecha_hoy, 'informacion':informacion, 'informacion_arm':informacion_arm})

@login_required
def parametros(request):
    form_sub_cliente = FormSubCliente()
    form_personal_deposito = FormPersonalDeposito()
    form_sector = FormSector()
    
    if request.method == 'POST':
        if 'btn_sub_cliente' in request.POST:
            form_sub_cliente = FormSubCliente(request.POST)
            if form_sub_cliente.is_valid():
                informacion = form_sub_cliente.cleaned_data
                sub_en_base = SubClientes.objects.filter(codigo=informacion['codigo'])
                if sub_en_base:
                    msj = 'El sub cliente ' + informacion['razon_social'] + ' ya se encuentra dado de alta.'
                    return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    

                sub_cliente = SubClientes(
                    codigo = informacion['codigo'],
                    cia_asociada = informacion['cia_asociada'],
                    razon_social = informacion['razon_social']
                    
                )
                sub_cliente.save()
                msj = 'Sub cliente ' + informacion['razon_social'] + ' creado exitosamente'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    
            else:
                msj = 'Formulario inválido'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    
        
        elif 'btn_sector' in request.POST:
            form_sector = FormSector(request.POST)
            if form_sector.is_valid():
                informacion = form_sector.cleaned_data
                sector_en_base = SectorDepo.objects.filter(descripcion=informacion['descripcion'])
                if sector_en_base:
                    msj = 'El sector ' + informacion['descripcion'] + ' ya se encuentra dado de alta.'
                    return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    

                sector = SectorDepo(
                    descripcion = informacion['descripcion']
                    
                )
                sector.save()
                msj = 'Sector ' + informacion['descripcion'] + ' creado exitosamente'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    
            else:
                msj = 'Formulario inválido'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    
        
        elif 'btn_personal_deposito' in request.POST:
            form_personal_deposito = FormPersonalDeposito(request.POST)
            if form_personal_deposito.is_valid():
                informacion = form_personal_deposito.cleaned_data
                personal_en_base = PersonalDeposito.objects.filter(dni=informacion['dni'])
                if personal_en_base:
                    msj = 'El empleado ' + informacion['nombre'] + ' ' + informacion['apellido'] +' con dni' + str(informacion['dni']) + ' ya se encuentra dado de alta.'
                    return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    

                empleado = PersonalDeposito(
                    dni = informacion['dni'],
                    nombre = informacion['nombre'],
                    apellido = informacion['apellido'],
                    sector = informacion['sector'],
                    
                )
                empleado.save()
                msj = 'Empleado con dni ' + str(informacion['dni']) + ' creado exitosamente'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    
            else:
                msj = 'Formulario inválido'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    
        
    
    
    
    msj = 'Ingrese los datos solicitados'
    return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    
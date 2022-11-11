from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FormNuevoPK, FormSubCliente, FormPersonalDeposito, FormSector, FormFinalizarPK, FormFinalizarArm
from .models import GlobalPK, SectorDepo, SubClientes, PersonalDeposito
from datetime import datetime



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
            pk_finalizado = GlobalPK.objects.get(numero=informacion['numero'])
            
            if pk_finalizado.estado_picking == 'Pendiente':
                msj = 'El global nro ' + informacion['numero'] + ' no se encuentra con el picking finalizado'
                return render(request, 'informes/finalizar_armado.html', {'msj':msj, 'form':form})
            
            
                
            pk_finalizado.estado_armado = 'Finalizado'
            pk_finalizado.fecha_armado = informacion['fecha_armado']
            
            if informacion['hora_fin_armado']:
                pk_finalizado.hora_fin_armado = informacion['hora_fin_armado']
            else:
                pk_finalizado.hora_fin_armado = '00:00:00'
                
            
            pk_finalizado.save()
            msj = 'Globlal ' + informacion['numero'] + ': Armado finalizado.'
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
            global_en_base = GlobalPK.objects.filter(numero=informacion['numero'])
            
            if not global_en_base:
                msj = 'No existe el numero de global ' + str(informacion['numero'])
                return render(request, 'informes/finalizar_global.html',{'form':form, 'msj':msj})
            
            global_finalizado = GlobalPK.objects.get(numero=informacion['numero'])
            
            global_finalizado.estado_picking = 'Finalizado'
            global_finalizado.operario = informacion['operario']
            global_finalizado.fecha_picking = informacion['fecha_picking']
            global_finalizado.hora_inicio_picking = informacion['hora_inicio_picking']
            global_finalizado.hora_fin_picking = informacion['hora_fin_picking']
            
            global_finalizado.save()
            msj = 'Global numero ' + informacion['numero'] + ' finalizado correctamente'
            return render(request, 'informes/finalizar_global.html',{'msj':msj, 'form':form})
        else:
            msj = 'Formulario invalido'
            return render(request, 'informes/finalizar_global.html',{'msj':msj, 'form':form})
        
    msj = 'Llene los datos solicitados'
    return render(request, 'informes/finalizar_global.html',{'msj':msj, 'form':form})



@login_required
def index_informes(request):
    return render(request, 'informes/index_informes.html')


def nuevo_global(request):
    
    if request.method == 'POST':
        form = FormNuevoPK(request.POST)

        if form.is_valid():
            
            
            informacion = form.cleaned_data
            validar_global = informacion['numero']
            global_en_base = GlobalPK.objects.filter(numero=validar_global)
            if global_en_base:
                picking = GlobalPK(
                    numero = informacion['numero'],
                    cliente = informacion['cliente'],
                    sub_cliente = informacion['sub_cliente'],
                    unidades = informacion['unidades'],
                    fecha_procesado = informacion['fecha_procesado'],
                    hora_procesado = informacion['hora_procesado'],
                    operario = informacion['operario'],
                    fecha_picking = informacion['fecha_picking'],
                    hora_inicio_picking = informacion['hora_inicio_picking'],
                    hora_fin_picking = informacion['hora_fin_picking'],
                    estado_picking = 'Pendiente',
                    estado_armado = 'Pendiente',
                    
                    
                )

                picking.save()
                msj = 'Global ' + informacion['numero'] + ' creado exitosamente'
                return render(request, 'informes/nuevo_global.html',{'form':form, 'msj':msj})
            else:
                msj = 'El numero' + informacion['numero'] + ' ya existe en la base de datos'
                return render(request, 'informes/nuevo_global.html',{'form':form, 'msj':msj})
            
        msj = 'Formulario inválido'
        return render(request, 'informes/nuevo_global.html',{'form':form, 'msj':msj})
    
    else:
        form = FormNuevoPK()
        msj = 'Llene los campos solicitados'
    
        return render(request, 'informes/nuevo_global.html',{'form':form, 'msj':msj})



@login_required
def informe_global(request):
    return render(request, 'informes/informe_global.html')

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
        
        elif 'btn_sector_deposito' in request.POST:
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
                    msj = 'El empleado ' + informacion['nombre'] + ' ' + informacion['apellido'] +' con dni' + informacion['dni'] + ' ya se encuentra dado de alta.'
                    return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    

                empleado = PersonalDeposito(
                    dni = informacion['dni'],
                    nombre = informacion['nombre'],
                    apellido = informacion['apellido'],
                    sector = informacion['sector'],
                    
                )
                empleado.save()
                msj = 'Empleado con dni ' + informacion['dni'] + ' creado exitosamente'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    
            else:
                msj = 'Formulario inválido'
                return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    
        
    
    
    
    msj = 'Ingrese los datos solicitados'
    return render(request, 'informes/crear_parametros.html', {'form_sub_cliente':form_sub_cliente, 'form_personal_deposito':form_personal_deposito, 'form_sector':form_sector, 'msj':msj})    
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import MasDatosUsuario

from empleados.models import Categoria, EmpleadoMeli, Fichero, Sucursal, TipoTarifa
from .forms import FormAltaPersonalMeli, FicharPersonalMeli, CrearCategoria, FormBusquedaFichero, FormEditarFicha, FormTipoTarifa, FormSucursal
# Create your views here.
from datetime import datetime
from .funciones import validar_dato



formato_fecha = "%d/%m/%Y %H:%M:%S"
formato_fecha2 = "%d/%m/%Y"
hoy = datetime.today()

   

@login_required
def index_meli(request):
    return render(request, 'empleados/index_meli.html')

@login_required
def linkeo(request):
    return render(request, 'index_new.html')

@login_required
def alta_personal_meli(request):
    
    if request.method == 'POST':
        
        form_alta = FormAltaPersonalMeli(request.POST)
        user = request.user
        
        if form_alta.is_valid():
            informacion = form_alta.cleaned_data
            empleado_en_base = EmpleadoMeli.objects.filter(dni=informacion['dni'])
            
            if not empleado_en_base:
                empleado = EmpleadoMeli(
                    dni = informacion['dni'],
                    nombre = informacion['nombre'],
                    apellido = informacion['apellido'],
                    banco = informacion['banco'],
                    alias = informacion['alias'],
                    sucursal_por_defecto = informacion['sucursal_por_defecto'],
                    alta_por = user,
                    fecha_alta = hoy
                    
                )
                
                if informacion['cbu']:
                    if len(informacion['cbu'])==22:
                        consulta = informacion['cbu']
                        validacion = validar_dato(consulta=consulta)
                        if validacion:
                            empleado.cbu = consulta
                        else:
                            msj = 'El CBU contiene caracteres invalidos'
                            return render(request, 'empleados/alta_personal_meli.html', {'msj':msj, 'form_alta':form_alta})
                    else: 
                        msj = 'Debe ingresar un CBU con 22 dígitos'
                        return render(request, 'empleados/alta_personal_meli.html', {'msj':msj, 'form_alta':form_alta})
                        
                else:
                    empleado.cbu = 0
                            
                            
                if informacion['alias']:
                    empleado.cbu = consulta
                else:
                    empleado.alias = ''

                
                
                empleado.save()
                msj = 'Nombre ' + informacion['nombre'] + ' ' + informacion['apellido'] + ' creado exitosamente.'
                return render(request, 'empleados/alta_personal_meli.html', {'msj':msj, 'form_alta':form_alta})
            else:
                msj = 'El DNI ya se encuentra dado de alta.'
                return render(request, 'empleados/alta_personal_meli.html',{'msj':msj, 'form_alta': form_alta})
        else:
            msj = 'Formulario invalido, verifique'
            return render(request, 'empleados/alta_personal_meli.html', {'form_alta':form_alta, 'msj':msj})
    else:
        form_alta = FormAltaPersonalMeli()
        msj = 'Ingrese los datos solicitados.'
        return render(request, 'empleados/alta_personal_meli.html', {'form_alta':form_alta, 'msj':msj})
    
    
@login_required
def alta_categoria(request):
    form_cat = CrearCategoria()
    form_tipo_tarifa = FormTipoTarifa()
    form_sucursal = FormSucursal()
    
    msj = 'Ingrese los datos solicitados.'
    
    if request.method == 'POST':
        
        
        
        
        if 'btn_cat' in request.POST:
            form_cat = CrearCategoria(request.POST)
            if form_cat.is_valid():

                informacion = form_cat.cleaned_data
                
                
                categoria_en_base = Categoria.objects.filter(categoria=informacion['categoria'])
                
                if not categoria_en_base:
                    nueva_categoria = Categoria(
                        categoria = informacion['categoria'],
                        tarifa_por_dia = informacion['tarifa_por_dia'],
                        
                    )
                    nueva_categoria.save()
                    msj = 'Categoria ' + informacion['categoria'] + ' creada exitosamente.'
                    return render(request, 'empleados/alta_categoria.html', {'msj':msj, 'form_cat':form_cat, 'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal})
                else:
                    msj = 'La categoria ' + informacion['categoria'] + ' ya se encuentra dada de alta.'
                    return render(request, 'empleados/alta_categoria.html',{'msj':msj, 'form_cat': form_cat, 'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal})
            else:
                msj = 'Formulario invalido, verifique'
                return render(request, 'empleados/alta_categoria.html', {'form_cat':form_cat, 'msj':msj, 'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal})
        
        
        
        
        elif 'btn_sucursal' in request.POST:
            form_sucursal = FormSucursal(request.POST)
            if form_sucursal.is_valid():

                informacion = form_sucursal.cleaned_data
                
                
                sucursal_en_base = Sucursal.objects.filter(sucursal=informacion['sucursal'])
                
                if not sucursal_en_base:
                    nueva_sucursal = Sucursal(
                        sucursal = informacion['sucursal'],
                        
                        
                    )
                    nueva_sucursal.save()
                    msj = 'Sucursal ' + informacion['sucursal'] + ' creada exitosamente.'
                    return render(request, 'empleados/alta_categoria.html', {'msj':msj, 'form_cat':form_cat, 'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal})
                else:
                    msj = 'La sucursal ' + informacion['sucursal'] + ' ya se encuentra dada de alta.'
                    return render(request, 'empleados/alta_categoria.html',{'msj':msj, 'form_cat': form_cat, 'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal})
            else:
                msj = 'Formulario invalido, verifique'
                return render(request, 'empleados/alta_categoria.html', {'form_cat':form_cat, 'msj':msj, 'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal})
        
        
        
        
        
        
        elif 'btn_tipotarifa' in request.POST:
            form_tipo_tarifa = FormTipoTarifa(request.POST)
            
            if form_tipo_tarifa.is_valid():
                
                informacion = form_tipo_tarifa.cleaned_data
                
                
                tarifa_en_base = TipoTarifa.objects.filter(tipo=informacion['tipo'])
                
                if not tarifa_en_base:
                    nueva_tarifa = TipoTarifa(
                        tipo = informacion['tipo'],
                        valor = informacion['valor'],
                        
                    )
                    nueva_tarifa.save()
                    msj = 'Tipo de tarifa ' + informacion['tipo'] + ' creada exitosamente.'
                    return render(request, 'empleados/alta_categoria.html', {'msj':msj, 'form_cat':form_cat, 'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal})
                else:
                    msj = 'El tipo de tarifa ' + informacion['tipo'] + ' ya se encuentra dado de alta.'
                    return render(request, 'empleados/alta_categoria.html',{'msj':msj, 'form_cat': form_cat, 'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal})
            else:
                msj = 'Formulario invalido, verifique'
                return render(request, 'empleados/alta_categoria.html', {'form_cat':form_cat, 'msj':msj, 'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal})
            
            
    else:
        
        msj = 'Ingrese los datos solicitados.'
        return render(request, 'empleados/alta_categoria.html', {'form_cat':form_cat, 'msj':msj, 'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal})
        
        
        
@login_required
def fichero(request):
    user = request.user
    mi_sucursal, _ = MasDatosUsuario.objects.get_or_create(user=user)
    
    form_fichero = FicharPersonalMeli(initial={
        'dni': '',
        'fecha_trabajada': hoy.strftime(formato_fecha2),
        'categoria': '',
        'tipo_tarifa': '',
        'sucursal': mi_sucursal,
        
    })
    
    msj = 'Ingrese los datos solicitados.'
    
    if request.method == 'POST':
        form_fichero = FicharPersonalMeli(request.POST)
        
        if form_fichero.is_valid():
            informacion = form_fichero.cleaned_data
            validar_personal = EmpleadoMeli.objects.filter(dni=informacion['dni'])
            if validar_personal:
                anti_reefichaje = Fichero.objects.filter(dni=informacion['dni'])
                validar_fecha = anti_reefichaje.filter(fecha_trabajada=informacion['fecha_trabajada'])
                validar_categoria = Categoria.objects.filter(categoria=informacion['categoria'])
                if validar_categoria:
                    if not validar_fecha:
                        
                        personal, _ = EmpleadoMeli.objects.get_or_create(dni=informacion['dni'])
                        costo, _ = Categoria.objects.get_or_create(categoria=informacion['categoria'])
                        
                        if informacion['tipo_tarifa']:
                            aumento, _ = TipoTarifa.objects.get_or_create(tipo=informacion['tipo_tarifa'])
                        else:
                            aumento = 0
                        
                        if aumento:
                            suma = aumento.valor + costo.tarifa_por_dia
                        else:
                            suma = aumento + costo.tarifa_por_dia
                            
                            
                        if informacion['sucursal']:
                            sucursal_trabajada = informacion['sucursal']
                        else:
                            sucursal_trabajada = personal.sucursal_por_defecto

                        
                                
                                                    
                        fichar = Fichero(
                            
                            dni = informacion['dni'],
                            fecha_trabajada = informacion['fecha_trabajada'],
                            
                            categoria = informacion['categoria'],
                            
                            nombre = personal.nombre,
                            apellido = personal.apellido,
                            tarifa = costo.tarifa_por_dia,
                            tipo_tarifa = str(informacion['tipo_tarifa']), 
                            total_dia = suma,
                            creado_por = request.user,
                            fecha_creacion = datetime.today(),
                            sucursal = sucursal_trabajada,
                            responsable = personal.alta_por,
                            editado = 'No',
                            cbu = personal.cbu,
                            pago_realizado = 'No',
                            alias = personal.alias,
                            
                            
                            
                            
                        )
                        
                            
                        
                        

                            
                        
                            
                            
                        if aumento:
                            fichar.suma_a_tarifa = aumento.valor
                        else:
                            fichar.suma_a_tarifa = 0
                        
                        
                        fichar.save()
                        msj = 'Fichero grabado'
                        return render(request, 'empleados/fichero.html', {'form_fichero':form_fichero, 'msj':msj})
                    else:
                        msj = 'Ya ingreso un fichaje de este individuo con esta fecha.'
                        return render(request, 'empleados/fichero.html', {'form_fichero':form_fichero, 'msj':msj})
                else:
                    msj = 'Categoria inexistente'
                    return render(request, 'empleados/fichero.html', {'form_fichero':form_fichero, 'msj':msj})
            else:
                msj = 'Numero de documento no encontrado'
                return render(request, 'empleados/fichero.html', {'form_fichero':form_fichero, 'msj':msj})
        else:
            msj = 'Formulario invalido'
            return render(request, 'empleados/fichero.html', {'form_fichero':form_fichero, 'msj':msj})
                    

    
    return render(request, 'empleados/fichero.html', {'form_fichero':form_fichero, 'msj':msj})




@login_required
def editar_fichero(request):
    #esta es mi vista de busqueda :P
    
    dni = request.GET.get('dni')
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')
    form = FormBusquedaFichero()
    
    if dni and not fecha_desde and not fecha_hasta:
        form = FormBusquedaFichero()
        ficheros_listado = Fichero.objects.filter(dni=dni)
        if ficheros_listado:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':ficheros_listado} )
        else:
            msj = 'Documento inexistente'
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj} )
        
    elif not dni and fecha_desde and not fecha_hasta:
        
        fecha_hasta = datetime.today()
        
        
        fecha_desde_formateada = datetime.strptime(fecha_desde + " 00:00:00", "%d/%m/%Y %H:%M:%S") #1
        dni = Fichero.objects.all()
        resultado_busqueda = []
        for valor in dni:
            fecha_trabajada_formateada = valor.fecha_trabajada.strftime(formato_fecha)
            fecha_trabajada_formateada_b = datetime.strptime(fecha_trabajada_formateada, "%d/%m/%Y %H:%M:%S")
            
            if fecha_trabajada_formateada_b >= fecha_desde_formateada and fecha_hasta >= fecha_trabajada_formateada_b:
                resultado_busqueda.append(valor)
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta.strftime(formato_fecha2)
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
            
        
    elif not dni and not fecha_desde and fecha_hasta:
        fecha_desde = '01/01/2020 00:00:00'
        fecha_desde_formateada = datetime.strptime(fecha_desde, "%d/%m/%Y %H:%M:%S")
        
        fecha_hasta_formateada = datetime.strptime(fecha_hasta + " 00:00:00", "%d/%m/%Y %H:%M:%S") #1
        
        dni = Fichero.objects.all()
        resultado_busqueda = []
       
        for valor in dni:
            fecha_trabajada_formateada = valor.fecha_trabajada.strftime(formato_fecha)
            fecha_trabajada_formateada_b = datetime.strptime(fecha_trabajada_formateada, "%d/%m/%Y %H:%M:%S")
            if fecha_trabajada_formateada_b >= fecha_desde_formateada and fecha_hasta_formateada >= fecha_trabajada_formateada_b:
                
                resultado_busqueda.append(valor)
                
                
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos hasta la fecha ' + fecha_hasta
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
       
       
       
    elif dni and fecha_desde and fecha_hasta:
        
        fecha_hasta_formateada = datetime.strptime(fecha_hasta + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        fecha_desde_formateada = datetime.strptime(fecha_desde + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        
        ficha = Fichero.objects.filter(dni=dni)
        resultado_busqueda = []
        for valor in ficha:
            
            fecha_trabajada_formateada = valor.fecha_trabajada.strftime(formato_fecha)
            fecha_trabajada_formateada_b = datetime.strptime(fecha_trabajada_formateada, "%d/%m/%Y %H:%M:%S")
            
            if fecha_trabajada_formateada_b >= fecha_desde_formateada and fecha_trabajada_formateada_b <= fecha_hasta_formateada:
                resultado_busqueda.append(valor)
        
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
    
    elif not dni and fecha_desde and fecha_hasta:
        fecha_hasta_formateada = datetime.strptime(fecha_hasta + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        fecha_desde_formateada = datetime.strptime(fecha_desde + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        dni = Fichero.objects.all()
        resultado_busqueda = []


        for valor in dni:
            fecha_trabajada_formateada = valor.fecha_trabajada.strftime(formato_fecha)
            fecha_trabajada_formateada_b = datetime.strptime(fecha_trabajada_formateada, "%d/%m/%Y %H:%M:%S")
            if fecha_trabajada_formateada_b >= fecha_desde_formateada and fecha_trabajada_formateada_b <= fecha_hasta_formateada:
                resultado_busqueda.append(valor)
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
    
    elif dni and fecha_desde and not fecha_hasta:
        fecha_desde_formateada = datetime.strptime(fecha_desde + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        fecha_hasta = datetime.today()
        
        dni = Fichero.objects.filter(dni=dni)
        
        
    
        resultado_busqueda = []
        
        
        for valor in dni:
            fecha_trabajada_formateada = valor.fecha_trabajada.strftime(formato_fecha)
            fecha_trabajada_formateada_b = datetime.strptime(fecha_trabajada_formateada, "%d/%m/%Y %H:%M:%S")
            
            
            if fecha_trabajada_formateada >= fecha_desde_formateada and fecha_trabajada_formateada <= fecha_hasta:
                resultado_busqueda.append(valor)
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta.strftime(formato_fecha)
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
    
    elif dni and not fecha_desde and fecha_hasta:
        
        dni = Fichero.objects.filter(dni=dni)
        fecha_desde = '01/01/2020 00:00:00'
        fecha_desde_formateada = datetime.strptime(fecha_desde, "%d/%m/%Y %H:%M:%S")
        fecha_hasta_formateada = datetime.strptime(fecha_hasta + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        
    
        resultado_busqueda = []
        for valor in dni:
            
            fecha_trabajada_formateada = valor.fecha_trabajada.strftime(formato_fecha)
            fecha_trabajada_formateada_b = datetime.strptime(fecha_trabajada_formateada, "%d/%m/%Y %H:%M:%S")
            
            if fecha_trabajada_formateada_b >= fecha_desde_formateada and fecha_trabajada_formateada_b <= fecha_hasta_formateada:
                resultado_busqueda.append(valor)
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
        
    
    # elif not dni and not fecha_desde and not fecha_hasta:
    #     form = FormBusquedaFichero()
    #     ficheros_listado = Fichero.objects.all()
    #     if ficheros_listado:
    #         return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':ficheros_listado} )
    #     else:
    #         msj = 'Sin datos'
    #         return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj} )
    
    
    
    else:
        msj = 'Busqueda: llene 1 o mas campos'
        return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj} )
    
    
    
    
    
@login_required
def edicion_fichero(request, id):
    
    ficha = Fichero.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormEditarFicha(request.POST)
        if form.is_valid():
            
            ficha.fecha_trabajada = form.cleaned_data.get('fecha_trabajada')
            ficha.dni = form.cleaned_data.get('dni')
            ficha.categoria = str(form.cleaned_data.get('categoria'))
            ficha.tarifa = form.cleaned_data.get('tarifa')
            
            
            ficha.save()
            msj = 'Ficha editada correctamente'
            return render(request, 'empleados/edicion_ficha.html', {'form': form, 'msj':msj, 'ficha':ficha})
        
        else:
            msj = 'Formulario incorrecto'
            return render(request, 'empleados/edicion_ficha.html', {'form': form, 'msj':msj, 'ficha':ficha})

    
    
    
    form_ficha = FormEditarFicha(initial={
        'fecha_trabajada': ficha.fecha_trabajada,
        'dni': ficha.dni,
        'categoria': ficha.categoria,
        'tarifa': ficha.tarifa, 
        
        })
    msj = 'Edicion de ficha de ' + ficha.nombre + ' ,' + ficha.apellido
    return render(request, 'empleados/edicion_ficha.html', {'form':form_ficha, 'msj':msj, 'ficha':ficha})




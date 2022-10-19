
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from empleados.models import Categoria, EmpleadoMeli, Fichero, TipoTarifa
from .forms import FormAltaPersonalMeli, FicharPersonalMeli, CrearCategoria, FormBusquedaFichero, FormEditarFicha, FormTipoTarifa
# Create your views here.
from datetime import datetime

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
        
        if form_alta.is_valid():
            informacion = form_alta.cleaned_data
            empleado_en_base = EmpleadoMeli.objects.filter(dni=informacion['dni'])
            
            if not empleado_en_base:
                empleado = EmpleadoMeli(
                    dni = informacion['dni'],
                    nombre = informacion['nombre'],
                    apellido = informacion['apellido']
                )
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
                    return render(request, 'empleados/alta_categoria.html', {'msj':msj, 'form_cat':form_cat, 'form_tipo_tarifa':form_tipo_tarifa})
                else:
                    msj = 'La categoria ' + informacion['categoria'] + ' ya se encuentra dada de alta.'
                    return render(request, 'empleados/alta_categoria.html',{'msj':msj, 'form_cat': form_cat, 'form_tipo_tarifa':form_tipo_tarifa})
            else:
                msj = 'Formulario invalido, verifique'
                return render(request, 'empleados/alta_categoria.html', {'form_cat':form_cat, 'msj':msj, 'form_tipo_tarifa':form_tipo_tarifa})
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
                    return render(request, 'empleados/alta_categoria.html', {'msj':msj, 'form_cat':form_cat, 'form_tipo_tarifa':form_tipo_tarifa})
                else:
                    msj = 'El tipo de tarifa ' + informacion['tipo'] + ' ya se encuentra dado de alta.'
                    return render(request, 'empleados/alta_categoria.html',{'msj':msj, 'form_cat': form_cat, 'form_tipo_tarifa':form_tipo_tarifa})
            else:
                msj = 'Formulario invalido, verifique'
                return render(request, 'empleados/alta_categoria.html', {'form_cat':form_cat, 'msj':msj, 'form_tipo_tarifa':form_tipo_tarifa})
            
            
    else:
        
        msj = 'Ingrese los datos solicitados.'
        return render(request, 'empleados/alta_categoria.html', {'form_cat':form_cat, 'msj':msj, 'form_tipo_tarifa':form_tipo_tarifa})
        
        
        
@login_required
def fichero(request):
    form_fichero = FicharPersonalMeli()
    
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
                        
                        fichar = Fichero(
                            
                            dni = informacion['dni'],
                            fecha_trabajada = informacion['fecha_trabajada'],
                            
                            categoria = informacion['categoria'],
                            
                            nombre = personal.nombre,
                            apellido = personal.apellido,
                            tarifa = costo.tarifa_por_dia,
                            tipo_tarifa = str(informacion['tipo_tarifa']),
                            
                            total_dia = suma
                            
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
        fecha_hasta = datetime.now()
        fecha_hasta_a = fecha_hasta.strftime("%d/%m/%Y")
        dni = Fichero.objects.all()
        resultado_busqueda = []
        for valor in dni:
            fecha_str = valor.fecha_trabajada.strftime("%d/%m/%Y")
            if fecha_str >= fecha_desde and fecha_hasta_a >= fecha_str:
                resultado_busqueda.append(valor)
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta_a
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
            
        
    elif not dni and not fecha_desde and fecha_hasta:
        fecha_desde = '01/01/2020'
        dni = Fichero.objects.all()
        resultado_busqueda = []
        for valor in dni:
            fecha_str = valor.fecha_trabajada.strftime("%d/%m/%Y")
            if fecha_str >= fecha_desde and fecha_hasta >= fecha_str:
                
                resultado_busqueda.append(valor)
                resultado_busqueda.append(fecha_str)
                
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
       
    elif dni and fecha_desde and fecha_hasta:
        ficha = Fichero.objects.filter(dni=dni)
        resultado_busqueda = []
        for valor in ficha:
            fecha = valor.fecha_trabajada.strftime("%d/%m/%Y")
            if fecha >= fecha_desde and fecha <= fecha_hasta:
                resultado_busqueda.append(valor)
        
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
    
    elif not dni and fecha_desde and fecha_hasta:
        dni = Fichero.objects.all()
        resultado_busqueda = []
        
        for valor in dni:
            fecha = valor.fecha_trabajada.strftime("%d/%m/%Y")
            if fecha >= fecha_desde and fecha <= fecha_hasta:
                resultado_busqueda.append(valor)
                
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
    
    elif dni and fecha_desde and not fecha_hasta:
        
        dni = Fichero.objects.filter(dni=dni)
        fecha_hasta = datetime.now()
        fecha_hasta_a = fecha_hasta.strftime("%d/%m/%Y")
    
        resultado_busqueda = []
        for valor in dni:
            fecha = valor.fecha_trabajada.strftime("%d/%m/%Y")
            if fecha >= fecha_desde and fecha <= fecha_hasta_a:
                resultado_busqueda.append(valor)
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta_a
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
    
    elif dni and not fecha_desde and fecha_hasta:
        dni = Fichero.objects.filter(dni=dni)
        fecha_desde = '01/01/2020'
    
        resultado_busqueda = []
        for valor in dni:
            fecha = valor.fecha_trabajada.strftime("%d/%m/%Y")
            if fecha >= fecha_desde and fecha <= fecha_hasta:
                resultado_busqueda.append(valor)
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
        
    
    
    
    
    
    
    
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
        'categoria': '',
        'tarifa': ficha.tarifa, 
        
        })
    msj = 'Edicion de ficha de ' + ficha.nombre + ' ,' + ficha.apellido + ' del dia '
    return render(request, 'empleados/edicion_ficha.html', {'form':form_ficha, 'msj':msj, 'ficha':ficha})




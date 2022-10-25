from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import MasDatosUsuario

from empleados.models import Categoria, EmpleadoMeli, Fichero, Sucursal, TipoTarifa
from .forms import FormAltaPersonalMeli, FicharPersonalMeli, CrearCategoria, FormBuscarCategoria, FormBuscarSucursal, FormBuscarTarifa, FormBusquedaFichero, FormEditarFicha, FormTipoTarifa, FormSucursal, FormVerPersonal
from datetime import datetime
from .funciones import validar_dato
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView



formato_fecha = "%d/%m/%Y %H:%M:%S"
formato_fecha2 = "%d/%m/%Y"
hoy = datetime.today()

@login_required
def editar_categoria(request, id):
    msj_sucursal = 'Busqueda de sucursal'
    msj_categoria = 'Busqueda de categoria'
    msj_tarifa = 'Busqueda de tipo de tarifa'
    
    form_categoria = FormBuscarCategoria()
    form_tipo_tarifa = FormBuscarTarifa()
    form_sucursal = FormBuscarSucursal()
        
    categoria = Categoria.objects.get(id=id)
    
    if request.method == 'POST':
        form = CrearCategoria(request.POST)
        if form.is_valid():
            
            categoria.categoria = form.cleaned_data.get('categoria')
            categoria.tarifa_por_dia = form.cleaned_data.get('tarifa_por_dia')           
            
    
            categoria.save()
            msj_vacio = 'Categoria editada correctamente'
            return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                                'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal, 'msj_vacio':msj_vacio})
        
        else:
            form = CrearCategoria(request.POST)
            msj = ''
            return render(request, 'empleados/editar_categoria.html', {'form': form, 'msj':msj, 'categoria':categoria})

    form = CrearCategoria(initial={
        'categoria': categoria.categoria,
        'tarifa_por_dia': categoria.tarifa_por_dia,
    
        })
    
    msj = 'Edicion de categoria: ' + categoria.categoria
    return render(request, 'empleados/editar_categoria.html', {'form':form, 'msj':msj, 'categoria':categoria})

@login_required
def editar_tarifa(request, id):
    msj_sucursal = 'Busqueda de sucursal'
    msj_categoria = 'Busqueda de categoria'
    msj_tarifa = 'Busqueda de tipo de tarifa'
    
    form_categoria = FormBuscarCategoria()
    form_tipo_tarifa = FormBuscarTarifa()
    form_sucursal = FormBuscarSucursal()
        
    tarifa = TipoTarifa.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormTipoTarifa(request.POST)
        if form.is_valid():
            
            tarifa.tipo = form.cleaned_data.get('tipo')
            tarifa.valor = form.cleaned_data.get('valor')           
    
            tarifa.save()
            msj_vacio = 'Tarifa editada correctamente'
            return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                                'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal, 'msj_vacio':msj_vacio})
        
        else:
            form = FormTipoTarifa(request.POST)
            msj = ''
            return render(request, 'empleados/editar_tarifa.html', {'form': form, 'msj':msj, 'tarifa':tarifa})

    form = FormTipoTarifa(initial={
        'tipo': tarifa.tipo,
        'valor': tarifa.valor,
    
        })
    
    msj = 'Edicion de tarifa: ' + tarifa.tipo
    return render(request, 'empleados/editar_tarifa.html', {'form':form, 'msj':msj, 'tarifa':tarifa})


@login_required
def editar_sucursal(request, id):
    msj_sucursal = 'Busqueda de sucursal'
    msj_categoria = 'Busqueda de categoria'
    msj_tarifa = 'Busqueda de tipo de tarifa'
    
    form_categoria = FormBuscarCategoria()
    form_tipo_tarifa = FormBuscarTarifa()
    form_sucursal = FormBuscarSucursal()
        
    sucursal = Sucursal.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormSucursal(request.POST)
        if form.is_valid():
            
            sucursal.sucursal = form.cleaned_data.get('sucursal')
                       
            sucursal.save()
            msj_vacio = 'Sucursal editada correctamente'
            return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                                'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal, 'msj_vacio':msj_vacio})
        
        else:
            form = FormSucursal(request.POST)
            msj = ''
            return render(request, 'empleados/editar_sucursal.html', {'form': form, 'msj':msj, 'sucursal':sucursal})

    form = FormSucursal(initial={
        'sucursal': sucursal.sucursal,
        })
    
    msj = 'Edicion de sucursal: ' + sucursal.sucursal
    return render(request, 'empleados/editar_sucursal.html', {'form':form, 'msj':msj, 'sucursal':sucursal})



class EliminarSucursal(LoginRequiredMixin ,DeleteView):
    model = Sucursal
    template_name = 'empleados/eliminar_sucursal.html'
    success_url = '/empleados/ver_parametros'
    
    
class EliminarCategoria(LoginRequiredMixin ,DeleteView):
    model = Categoria
    template_name = 'empleados/eliminar_categoria.html'
    success_url = '/empleados/ver_parametros'
    
    
class EliminarTarifa(LoginRequiredMixin ,DeleteView):
    model = TipoTarifa
    template_name = 'empleados/eliminar_tarifa.html'
    success_url = '/empleados/ver_parametros'
    
    
class EliminarFicha(LoginRequiredMixin ,DeleteView):
    model = Fichero
    template_name = 'empleados/eliminar_ficha.html'
    success_url = '/empleados/busqueda_fichero'
    
    
    
class EliminarPersonal(LoginRequiredMixin ,DeleteView):
    model = EmpleadoMeli
    template_name = 'empleados/eliminar_personal.html'
    success_url = '/empleados/ver_personal'
    
    
    


def ver_personal(request):
    object_list = EmpleadoMeli.objects.all()
    return render(request, 'empleados/ver_personal.html', {'object_list':object_list})


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
                    empleado.alias = informacion['alias']
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
def ver_parametros(request):
    msj_sucursal = 'Busqueda de sucursal'
    msj_categoria = 'Busqueda de categoria'
    msj_tarifa = 'Busqueda de tipo de tarifa'
    msj_vacio = 'Sin resultados de busqueda'
    
    form_categoria = FormBuscarCategoria()
    form_tipo_tarifa = FormBuscarTarifa()
    form_sucursal = FormBuscarSucursal()
    
    
    if 'btn_busqueda_sucursal' in request.GET:
        sucursal = request.GET.get('sucursal')
        sucursales = Sucursal.objects.filter(sucursal=sucursal)
        if sucursales:
            return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                                'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal, 'sucursales':sucursales})
        else:
            return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                                'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal, 'msj_vacio':msj_vacio})
    
    elif 'btn_todos_s' in request.GET:
        sucursales = Sucursal.objects.all()
        return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                            'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal, 'sucursales':sucursales})
    
    elif 'btn_busqueda_categoria' in request.GET:
        categoria = request.GET.get('categoria')
        categorias = Categoria.objects.filter(categoria=categoria)
        if categorias:
            return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                                    'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal, 'categorias':categorias})
        else:
            return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                                'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal, 'msj_vacio':msj_vacio})
        
    elif 'btn_todos_c' in request.GET:
        categorias = Categoria.objects.all()
        return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                                'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal, 'categorias':categorias})
       
    elif 'btn_busqueda_tarifa' in request.GET:
        tipo = request.GET.get('tipo')
        tipo_tarifa = TipoTarifa.objects.filter(tipo=tipo)
        if tipo_tarifa:
            return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                                    'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal, 'tipo_tarifa':tipo_tarifa})
        else:
            return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                                'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal, 'msj_vacio':msj_vacio})
        
    elif 'btn_todos_t' in request.GET:
        tipo_tarifa = TipoTarifa.objects.all()
        return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                                'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal, 'tipo_tarifa':tipo_tarifa})
    
    return render(request, 'empleados/ver_parametros.html',{'msj_sucursal': msj_sucursal, 'msj_categoria':msj_categoria, 'msj_tarifa':msj_tarifa, 'form_categoria':form_categoria,
                                                            'form_tipo_tarifa':form_tipo_tarifa, 'form_sucursal':form_sucursal})

@login_required
def ver_personal(request):
    personas = EmpleadoMeli.objects.all()
    dni = request.GET.get('dni')
    sucursal = request.GET.get('sucursal')
    form = FormVerPersonal()
    msj = 'Busqueda y edicion de personal MELI'
    
    if 'btn_todos' in request.GET:
        personas = EmpleadoMeli.objects.all()
        msj = 'Personal completo: '
        return render(request, 'empleados/ver_personal.html', {'personas':personas, 'msj':msj, 'form':form})
    
    if dni and not sucursal or dni and sucursal:
        personas = EmpleadoMeli.objects.filter(dni=dni)
        
        if sucursal:
            msj = 'Resultado de la busqueda: (Busqueda por DNI ignora sucursal)'
        else:
            msj = 'Resultado de la busqueda: '
            
        
        return render(request, 'empleados/ver_personal.html', {'personas':personas, 'msj':msj, 'form':form})
    
    elif not dni and sucursal:
        
        dni = EmpleadoMeli.objects.all()
        sucursal, _ = Sucursal.objects.get_or_create(id=sucursal)
        personas = []
        for valor in dni:
            if valor.sucursal_por_defecto == sucursal.sucursal:
                personas.append(valor)
                
        
        if personas:

        
            msj = 'Resultado de la busqueda: '
            return render(request, 'empleados/ver_personal.html', {'personas':personas, 'msj':msj, 'form':form})
        else:
            msj = 'Sin personas en sucursal'
            return render(request, 'empleados/ver_personal.html', {'msj':msj, 'form':form})
    else:
    
    
        return render(request, 'empleados/ver_personal.html', {'msj':msj, 'form':form})


@login_required
def busqueda_fichero(request):
    #esta es mi vista de busqueda :P
    
    dni = request.GET.get('dni')
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')
    sucursal = request.GET.get('sucursal')
    
    form = FormBusquedaFichero(initial={'dni':dni, 'fecha_desde':fecha_desde, 'fecha_hasta':fecha_hasta})
    
    if dni and not fecha_desde and not fecha_hasta and not sucursal:
        form = FormBusquedaFichero(initial={'dni':dni, 'fecha_desde':fecha_desde, 'fecha_hasta':fecha_hasta})
        ficheros_listado = Fichero.objects.filter(dni=dni)
        if ficheros_listado:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':ficheros_listado} )
        else:
            msj = 'Documento inexistente'
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj} )
        
    elif not dni and fecha_desde and not fecha_hasta and not sucursal:
        
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
            
        
    elif not dni and not fecha_desde and fecha_hasta and not sucursal:
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
       
       
       
    elif dni and fecha_desde and fecha_hasta and not sucursal:
        
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
    
    elif not dni and fecha_desde and fecha_hasta and not sucursal:
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
    
    elif dni and fecha_desde and not fecha_hasta and not sucursal:
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
    
    elif dni and not fecha_desde and fecha_hasta and not sucursal:
        
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
        


    
    #agrego condiciones para filtro por SUCURSAL
    #Con DNI con Sucursal Sin fecha desde sin fecha hasta
    elif dni and sucursal and not fecha_desde and not fecha_hasta:
        dni = Fichero.objects.filter(dni=dni)
        
        resultado_busqueda = []
        sucursal, _ = Sucursal.objects.get_or_create(id=sucursal)
        
        for valor in dni:
            
            if valor.sucursal == sucursal.sucursal:
                resultado_busqueda.append(valor)
                
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos'
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
    
    
    #Con DNI con Sucursal con fecha desde con fecha hasta
    elif dni and fecha_desde and fecha_hasta and sucursal:
        
        fecha_hasta_formateada = datetime.strptime(fecha_hasta + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        fecha_desde_formateada = datetime.strptime(fecha_desde + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        ficha = Fichero.objects.filter(dni=dni)

        resultado_busqueda = []
        sucursal, _ = Sucursal.objects.get_or_create(id=sucursal)
        
        for valor in ficha:
            if valor.sucursal == sucursal.sucursal:

                fecha_trabajada_formateada = valor.fecha_trabajada.strftime(formato_fecha)
                fecha_trabajada_formateada_b = datetime.strptime(fecha_trabajada_formateada, "%d/%m/%Y %H:%M:%S")
                
                if fecha_trabajada_formateada_b >= fecha_desde_formateada and fecha_trabajada_formateada_b <= fecha_hasta_formateada:
                    resultado_busqueda.append(valor)
                    
        if resultado_busqueda:
            
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos'
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
    
    #Con DNI con Sucursal Sin fecha desde con fecha hasta
    
    
    elif dni and sucursal and not fecha_desde and fecha_hasta:
        
        dni = Fichero.objects.filter(dni=dni)
        
        fecha_desde = '01/01/2020 00:00:00'
        fecha_desde_formateada = datetime.strptime(fecha_desde, "%d/%m/%Y %H:%M:%S")
        
        fecha_hasta_formateada = datetime.strptime(fecha_hasta + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        sucursal, _ = Sucursal.objects.get_or_create(id=sucursal)
        
        resultado_busqueda = []
        
        for valor in dni:
            if valor.sucursal == sucursal.sucursal:
                
                fecha_trabajada_formateada = valor.fecha_trabajada.strftime(formato_fecha)
                fecha_trabajada_formateada_b = datetime.strptime(fecha_trabajada_formateada, "%d/%m/%Y %H:%M:%S")
                
                if fecha_trabajada_formateada_b >= fecha_desde_formateada and fecha_trabajada_formateada_b <= fecha_hasta_formateada:
                    resultado_busqueda.append(valor)
        
                    
        if resultado_busqueda:
                
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos'
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
                
                
    #Con DNI con Sucursal con fecha desde sin fecha hasta
    elif dni and sucursal and fecha_desde and not fecha_hasta:
        
        fecha_desde_formateada = datetime.strptime(fecha_desde + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        fecha_hasta = datetime.today()
        dni = Fichero.objects.filter(dni=dni)
        resultado_busqueda = []
        sucursal, _ = Sucursal.objects.get_or_create(id=sucursal)
        
        for valor in dni:

            if valor.sucursal == sucursal.sucursal:
                fecha_trabajada_formateada = valor.fecha_trabajada.strftime(formato_fecha)
                fecha_trabajada_formateada_b = datetime.strptime(fecha_trabajada_formateada, "%d/%m/%Y %H:%M:%S")
            
                if fecha_trabajada_formateada >= fecha_desde_formateada and fecha_trabajada_formateada <= fecha_hasta:
                    resultado_busqueda.append(valor)
                
                
                
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta.strftime(formato_fecha)
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
        
    
    #Sin DNI con Sucursal Sin fecha desde sin fecha hasta
    elif not dni and sucursal and not fecha_desde and not fecha_hasta:
        
        dni = Fichero.objects.all()
        
        sucursal, _ = Sucursal.objects.get_or_create(id=sucursal)
        resultado_busqueda = []
        
        
        for valor in dni:
            if valor.sucursal == sucursal.sucursal:
                resultado_busqueda.append(valor)
                
        if resultado_busqueda:
                return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos en esta sucursal'
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
    
    #Sin DNI con Sucursal con fecha desde con fecha hasta
    elif not dni and sucursal and fecha_desde and fecha_hasta:
        
        fecha_hasta_formateada = datetime.strptime(fecha_hasta + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        fecha_desde_formateada = datetime.strptime(fecha_desde + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        dni = Fichero.objects.all()
        
        resultado_busqueda = []
        sucursal, _ = Sucursal.objects.get_or_create(id=sucursal)
        
        for valor in dni:
            if valor.sucursal == sucursal.sucursal:

                fecha_trabajada_formateada = valor.fecha_trabajada.strftime(formato_fecha)
                fecha_trabajada_formateada_b = datetime.strptime(fecha_trabajada_formateada, "%d/%m/%Y %H:%M:%S")
                
                if fecha_trabajada_formateada_b >= fecha_desde_formateada and fecha_trabajada_formateada_b <= fecha_hasta_formateada:
                    resultado_busqueda.append(valor)
                    
        if resultado_busqueda:
            
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos en la sucursal: ' + sucursal.sucursal + 'entre las fechas ' + fecha_desde + ' y ' + fecha_hasta
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
        
        
    #Sin DNI con Sucursal Sin fecha desde con fecha hasta
    elif not dni and sucursal and not fecha_desde and fecha_hasta:
        
        dni = Fichero.objects.all()
        fecha_desde = '01/01/2020 00:00:00'
        fecha_desde_formateada = datetime.strptime(fecha_desde, "%d/%m/%Y %H:%M:%S")
        
        fecha_hasta_formateada = datetime.strptime(fecha_hasta + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        sucursal, _ = Sucursal.objects.get_or_create(id=sucursal)
        
        resultado_busqueda = []
        
        for valor in dni:
            if valor.sucursal == sucursal.sucursal:
                fecha_trabajada_formateada = valor.fecha_trabajada.strftime(formato_fecha)
                fecha_trabajada_formateada_b = datetime.strptime(fecha_trabajada_formateada, "%d/%m/%Y %H:%M:%S")
                if fecha_trabajada_formateada_b >= fecha_desde_formateada and fecha_trabajada_formateada_b <= fecha_hasta_formateada:
                    resultado_busqueda.append(valor)
        if resultado_busqueda:
                
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos'
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
    
    #Sin DNI con Sucursal con fecha desde sin fecha hasta
    
    elif not dni and sucursal and fecha_desde and not fecha_hasta:
        
        fecha_desde_formateada = datetime.strptime(fecha_desde + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        fecha_hasta = datetime.today()
        dni = Fichero.objects.all()
        resultado_busqueda = []
        sucursal, _ = Sucursal.objects.get_or_create(id=sucursal)
        
        for valor in dni:

            if valor.sucursal == sucursal.sucursal:
                fecha_trabajada_formateada = valor.fecha_trabajada.strftime(formato_fecha)
                fecha_trabajada_formateada_b = datetime.strptime(fecha_trabajada_formateada, "%d/%m/%Y %H:%M:%S")
            
                if fecha_trabajada_formateada >= fecha_desde_formateada and fecha_trabajada_formateada <= fecha_hasta:
                    resultado_busqueda.append(valor)
                
                
                
        if resultado_busqueda:
            return render(request, 'empleados/editar_fichero.html', {'form':form,'ficheros_listado':resultado_busqueda})
        else:
            msj = 'Sin datos entre el rango ' + fecha_desde + ' hasta ' + fecha_hasta.strftime(formato_fecha) + 'en la sucursal ' + sucursal.sucursal
            return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj})
        
    else:
        msj = 'Busqueda: llene 1 o mas campos'
        return render(request, 'empleados/editar_fichero.html', {'form':form,'msj':msj} )
    
@login_required
def editar_personal(request, id):
    
    personal = EmpleadoMeli.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormAltaPersonalMeli(request.POST)
        if form.is_valid():
            personal.dni = form.cleaned_data.get('dni')
            personal.nombre = form.cleaned_data.get('nombre')
            personal.apellido = form.cleaned_data.get('apellido')
            personal.banco = form.cleaned_data.get('banco')
            personal.cbu = form.cleaned_data.get('cbu')
            personal.alias = form.cleaned_data.get('alias')
            personal.sucursal_por_defecto = str(form.cleaned_data.get('sucursal'))
            personal.save()
            msj = 'Personal editado correctamente.'
            return render(request, 'empleados/editar_personal.html', {'form':form, 'personal':personal, 'msj':msj})
        else:
            msj = 'Formulario inválido'
            return render(request, 'empleados/editar_personal.html', {'form':form, 'personal':personal, 'msj':msj})
    
    sucursal = str(personal.sucursal_por_defecto)
    form = FormAltaPersonalMeli(initial={
        'dni': personal.dni,
        'nombre': personal.nombre,
        'apellido': personal.apellido,
        'banco': personal.banco,
        'cbu': personal.cbu,
        'alias': personal.alias,
        'sucursal': sucursal
        
        })
    msj = 'Edicion de ficha de ' + personal.nombre + ' ,' + personal.apellido
    return render(request, 'empleados/editar_personal.html', {'form':form, 'msj':msj, 'personal':personal})




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
            ficha.editado = 'Si'
            ficha.fecha_de_edicion = datetime.today()
            
            
            
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
        'sucursal': ficha.sucursal,
        
        })
    msj = 'Edicion de ficha de ' + ficha.nombre + ' ,' + ficha.apellido
    return render(request, 'empleados/edicion_ficha.html', {'form':form_ficha, 'msj':msj, 'ficha':ficha})



def pagar_ficha(request, id):
    ficha = Fichero.objects.get(id=id)
    form = FormBusquedaFichero()
    
    ficha.pago_realizado = 'Si'
    
    ficha.fecha_de_edicion = datetime.today()
    
        
        
        
    ficha.save()
    msj = 'Pago computado'
    return render(request, 'empleados/editar_fichero.html', {'msj':msj, 'form':form})




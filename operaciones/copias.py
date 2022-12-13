
from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from operaciones.forms import FormCrearCatUb, FormCrearCatUbVal, FormCrearProducto, FormBusquedaProducto, FormEditarProducto, FormCrearCia, FormPack, FormCatPk, FormCatRepo, FormTipoAlm, FormPack, FormCubicaje, FormProducto, FormAforo
from datetime import datetime
from operaciones.models import CatUbicacionValor, Cia, Producto, TipoPack, CatPicking, CatUbicacion, CatRepo, TipoAlm, Cubicaje
import django_excel as excel

from django.contrib.auth.decorators import login_required









@login_required
def nuevo_aforo(request):
    
    
    if request.method == 'POST':
        form_crear_producto = FormCrearProducto(request.POST)
        if form_crear_producto.is_valid():

            informacion = form_crear_producto.cleaned_data
            
            validar_cia = informacion['cia']
            
            cia_en_base = Cia.objects.get(descripcion=validar_cia)
            
            if cia_en_base:
                
                peso_caja = float(informacion['peso_un']) * float(informacion['unidad_caja'])
                
                peso_pallet = float(informacion['peso_un']) * float(informacion['unidad_pall'])
                
                user = request.user
                
                validar_ub = CatUbicacion.objects.filter(cia_asociada=cia_en_base.cod)
                validar_pk = CatPicking.objects.filter(cia_asociada=cia_en_base.cod)
                validar_repo = CatRepo.objects.filter(cia_asociada=cia_en_base.cod)
                if validar_ub:
                    ub = CatUbicacion.objects.get(cia_asociada=cia_en_base.cod)
                else:
                    ub = False
                    
                if validar_pk:
                    pk = CatPicking.objects.get(cia_asociada=cia_en_base.cod)
                else:
                    pk = False
                    
                if validar_repo:
                    
                    repo = CatRepo.objects.get(cia_asociada=cia_en_base.cod)
                else:
                    repo = False
                    
                if not ub:
                    form_crear_producto = FormCrearProducto(informacion)
                    form_error = 'No existe categoria de ubicacion para la cia.'
                    return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, 'form2':form_error} )
                if not pk:
                    form_crear_producto = FormCrearProducto(informacion)
                    form_error = 'No existe categoria de picking para la cia.'
                    return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, 'form2':form_error} )
                if not repo:
                    form_crear_producto = FormCrearProducto(informacion)
                    form_error = 'No existe categoria de reposicion para la cia.'
                    return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, 'form2':form_error} )
                
                cia_grabar = Cia.objects.get(descripcion=informacion['cia'])
                
                if informacion['concesion']:
                    cons = Cia.objects.get(descripcion=informacion['concesion'])
                else:
                    cons = ''
                    
                producto = Producto(cia = cia_grabar.cod,
                                codigo = informacion['codigo'],
                                descripcion = informacion['descripcion'],
                                peso_un = informacion['peso_un'],
                                largo_un = informacion['largo_un'],
                                ancho_un = informacion['ancho_un'],
                                alto_un = informacion['alto_un'],
                                unidad_caja = informacion['unidad_caja'],
                                largo_cj = informacion['peso_un'],
                                ancho_cj = informacion['ancho_cj'],
                                alto_cj = informacion['alto_cj'],
                                unidad_pall = informacion['unidad_pall'],
                                usuario = user,
                                pack = informacion['pack'],
                                
                                vd = informacion['vd'],
                                cat_pk = pk.cod,
                                cat_repo = repo.cod,
                                cat_emb = '001',
                                clase = 'B',
                                unidad_minima = 1 ,
                                unidad_medida = '01',
                                fecha_creacion = datetime.now(),
                                tipo_alm = informacion['tipo_alm'],
                                )
                if cons != '':
                    producto.concesion = cons.cod
                else:
                    producto.concesion = ''
                
                if str(informacion['tipo_alm']) == 'Stock':
                    
                    producto.cat_ub = ub.cod
                    
                elif str(informacion['tipo_alm']) == 'Valor':
                    
                    validar_ubval = CatUbicacionValor.objects.filter(cia_asociada=informacion['cia'])
                    if validar_ubval:
                        ubval = CatUbicacionValor.objects.get(cia_asociada=informacion['cia'])
                    else:
                        ubval = False
                    if not ubval:
                        form_crear_producto = FormCrearProducto(informacion)
                        form_error = 'No existe categoria de ubicacion de valor para la cia.'
                        return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, 'form2':form_error} )
                    producto.cat_ub = ubval.cod
                    
                
                
                producto.peso_cj = peso_caja
                producto.peso_pall = peso_pallet
                producto.largo_pall = 1.2
                producto.ancho_pall = 1
                producto.alto_pall = 1.4
                producto.importado_saad = 'No'
                producto.importado_presis = 'No'
                
                
                
                
                
                
                cat_ub_sp = CatUbicacion.objects.get(cia_asociada='022')
                cat_pk_sp = CatPicking.objects.get(cia_asociada='022')
                cat_repo_sp = CatRepo.objects.get(cia_asociada='022')
                
                linea_022 = Producto(
                    cia = '022',
                    codigo = producto.codigo,
                    descripcion = producto.descripcion,
                    largo_pall = 1.2,
                    ancho_pall = 1.0,
                    alto_pall = 1.4,
                    peso_un = producto.peso_un,
                    largo_un = producto.largo_un,
                    ancho_un = producto.ancho_un,
                    alto_un = producto.alto_un,
                    unidad_caja = producto.unidad_caja,
                    largo_cj = producto.largo_cj,
                    alto_cj = producto.alto_cj,
                    ancho_cj = producto.ancho_cj,
                    unidad_pall = producto.unidad_pall,
                    pack = producto.pack,
                    vd = producto.vd,
                    tipo_alm = producto.tipo_alm,
                    fecha_creacion = datetime.now(),
                    usuario = user,
                    concesion = '',

                    cat_ub = cat_ub_sp.cod,
                    cat_pk = cat_pk_sp.cod,
                    cat_repo = cat_repo_sp.cod,
                    cat_emb = '001',
                    clase = 'B', #siempre B
                    unidad_minima = '1', #siempre 1
                    unidad_medida = '01', #siempre 01
                    peso_cj = producto.peso_cj, #multiplicacion de peso * unidad_caja
                    peso_pall = producto.peso_pall, #multiplicacion de peso * unidad_pall
                    

                    
                    importado_saad = 'No', #si o no 'para importar solo lo que hace falta en saad
                    importado_presis = 'No', #si o no 'para importar solo lo que hace falta en saad
    
                    
                    
                )
                
                
                
                
            
            
                cat_ub_rio = CatUbicacion.objects.get(cia_asociada='001')
                cat_pk_rio = CatPicking.objects.get(cia_asociada='001')
                cat_repo_rio = CatRepo.objects.get(cia_asociada='001')
                
                
                
                if informacion['concesion']:
                    concesion_de = Cia.objects.get(descripcion=informacion['concesion'])
                
                    linea_001 = Producto(
                        cia = concesion_de.cod,
                        codigo = producto.codigo,
                        descripcion = producto.descripcion,
                        largo_pall = 1.2,
                        ancho_pall = 1.0,
                        alto_pall = 1.4,
                        peso_un = producto.peso_un,
                        largo_un = producto.largo_un,
                        ancho_un = producto.ancho_un,
                        alto_un = producto.alto_un,
                        unidad_caja = producto.unidad_caja,
                        largo_cj = producto.largo_cj,
                        alto_cj = producto.alto_cj,
                        ancho_cj = producto.ancho_cj,
                        unidad_pall = producto.unidad_pall,
                        pack = producto.pack,
                        vd = producto.vd,
                        tipo_alm = producto.tipo_alm,
                        fecha_creacion = datetime.now(),
                        usuario = user,
                        concesion = '',

                        cat_ub = cat_ub_rio.cod,
                        cat_pk = cat_pk_rio.cod,
                        cat_repo = cat_repo_rio.cod,
                        cat_emb = '001',
                        clase = 'B', #siempre B
                        unidad_minima = '1', #siempre 1
                        unidad_medida = '01', #siempre 01
                        peso_cj = producto.peso_cj, #multiplicacion de peso * unidad_caja
                        peso_pall = producto.peso_pall, #multiplicacion de peso * unidad_pall
                        

                        
                        importado_saad = 'No', #si o no 'para importar solo lo que hace falta en saad
                        importado_presis = 'No', #si o no 'para importar solo lo que hace falta en saad
        
                        
                        
                    )
                    cubicaje = Cubicaje.objects.get(id=1)
                    volumen = producto.largo_un * producto.ancho_un * producto.alto_un * producto.unidad_pall
                    
                
                    if volumen > cubicaje.metro_cubico:
                        form_creado = 'Chequear valores Alto unidad= ' + str(producto.alto_un) + ' Ancho =' + str(producto.ancho_un) + ' Largo= ' + str(producto.alto_un) + ' Unidad por pallet= ' + str(producto.unidad_pall) + ' Total Volumen=' + str(volumen)
                        return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, 'form2':form_creado})
                
                    
                
                    linea_001.save()
                
                
                
                
                cubicaje = Cubicaje.objects.get(id=1)
                
                volumen = producto.largo_un * producto.ancho_un * producto.alto_un * producto.unidad_pall
                
                
                
                if volumen > cubicaje.metro_cubico:
                    form_creado = 'Chequear valores Alto unidad= ' + str(producto.alto_un) + ' Ancho =' + str(producto.ancho_un) + ' Largo= ' + str(producto.alto_un) + ' Unidad por pallet= ' + str(producto.unidad_pall) + ' Total Volumen=' + str(volumen)
                    return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, 'form2':form_creado})
                
                    
                linea_022.save()
                producto.save()
                
                
                
                
                
                
                
                
                form_crear_producto = FormCrearProducto()
                form_creado = 'Cod ' + producto.codigo + ' creado exitosamente'
                return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, 'form2':form_creado})
                
            else:
                form_crear_producto = FormCrearProducto(informacion)
                form_error = 'La CIA no existe, verifique...'
            return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, 'form2':form_error} )
        else:
            form_crear_producto = FormCrearProducto()
        return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto})
    form_crear_producto = FormCrearProducto()
    return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto})
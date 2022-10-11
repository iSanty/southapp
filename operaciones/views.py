from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from operaciones.forms import FormCrearCatUb, FormCrearProducto, FormBusquedaProducto, FormEditarProducto, FormCrearCia, FormPack, FormCatPk, FormCatRepo, FormTipoAlm, FormPack
from datetime import datetime
from operaciones.models import Cia, Producto, TipoPack, CatPicking, CatUbicacion, CatRepo, TipoAlm
import django_excel as excel

from django.contrib.auth.decorators import login_required


@login_required
def crear_parametros(request):
    formcia = FormCrearCia()
    formcatub = FormCrearCatUb()
    formcatrepo = FormCatRepo()
    formcatpk = FormCatPk()
    formtipoalm = FormTipoAlm()
    formpack = FormPack()
    
    if request.method == 'POST':
        
        
        #boton para crear pack
        if 'btn_pack' in request.POST:
            datos_pack = FormPack(request.POST)
            if datos_pack.is_valid():
                info = datos_pack.cleaned_data
                pack_en_base = TipoPack.objects.filter(desc=info['desc'])
                if pack_en_base:
                    pack_en_base = 'Pack ' + info['desc'] + ' ya se encuentra dado de alta'
                    return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':pack_en_base})
                pack = TipoPack(
                    desc = info['desc']
                    )
                pack.save()
                grabado = 'Pack ' + pack.desc + ' creado exitosamente.'
                return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':grabado})
            else:
                grabado = 'Formulario invalido'
                return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':grabado})
        #boton para crear pack
        #--------------------
        #boton para crear cia
        elif 'btn_cia' in request.POST:
            datos_cia = FormCrearCia(request.POST)
            if datos_cia.is_valid():
                info = datos_cia.cleaned_data
                cia_en_base = Cia.objects.filter(cod=info['cod'])
                if cia_en_base:
                    cia_en_base = 'Cia ' + info['cod']+ ' ' + info['descripcion'] + ' ya se encuentra dada de alta'
                    return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':cia_en_base})
                cia = Cia(
                    cod = info['cod'],
                    descripcion = info['descripcion']
                    )
                cia.save()
                grabado = 'Cia ' + cia.cod + ' creada exitosamente.'
                return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':grabado})
            else:
                grabado = 'Formulario invalido'
                return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':grabado})
        #boton para crear cia
        #--------------------
        #boton para crear cat de pk
        elif 'btn_catpk' in request.POST:
            datos_catpk = FormCatPk(request.POST)
            if datos_catpk.is_valid():
                info = datos_catpk.cleaned_data
                catpk_en_base = CatPicking.objects.filter(cod=info['cod'])
                if catpk_en_base:
                    catpk_en_base = 'Categoria de pk ' + info['cod']+ ' ' + info['descripcion'] + ' ya se encuentra dada de alta'
                    return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':catpk_en_base})
                catpk = CatPicking(
                    cod = info['cod'],
                    descripcion = info['descripcion']
                    )
                catpk.save()
                grabado = 'Categoria ' + catpk.cod + ' creada exitosamente.'
                return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':grabado})
            else:
                grabado = 'Formulario invalido'
                return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':grabado})
        #boton para crear cat de pk
        
        #boton para crear cat de ub
        elif 'btn_catub' in request.POST:
            datos_catub = FormCrearCatUb(request.POST)
            if datos_catub.is_valid():
                info = datos_catub.cleaned_data
                catub_en_base = CatUbicacion.objects.filter(cod=info['cod'])
                if catub_en_base:
                    catub_en_base = 'Categoria de ub ' + info['cod']+ ' ' + info['descripcion'] + ' ya se encuentra dada de alta'
                    return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':catub_en_base})
                catub = CatUbicacion(
                    cod = info['cod'],
                    descripcion = info['descripcion']
                    )
                catub.save()
                grabado = 'Categoria ' + catub.cod + ' creada exitosamente.'
                return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':grabado})
            else:
                grabado = 'Formulario invalido'
                return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':grabado})
        #boton para crear cat de ub
        
        #boton para crear cat de repo
        elif 'btn_catrepo' in request.POST:
            datos_catrepo = FormCatRepo(request.POST)
            if datos_catrepo.is_valid():
                info = datos_catrepo.cleaned_data
                catrepo_en_base = CatRepo.objects.filter(cod=info['cod'])
                if catrepo_en_base:
                    catrepo_en_base = 'Categoria de repo ' + info['cod']+ ' ' + info['descripcion'] + ' ya se encuentra dada de alta'
                    return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':catrepo_en_base})
                catrepo = CatRepo(
                    cod = info['cod'],
                    descripcion = info['descripcion']
                    )
                catrepo.save()
                grabado = 'Categoria ' + catrepo.cod + ' creada exitosamente.'
                return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':grabado})
            else:
                grabado = 'Formulario invalido'
                return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':grabado})
        #boton para crear cat de repo
        
        #boton para crear tipo alm
        elif 'btn_tipoalm' in request.POST:
            datos_tipoalm = FormTipoAlm(request.POST)
            if datos_tipoalm.is_valid():
                info = datos_tipoalm.cleaned_data
                tipoalm_en_base = TipoAlm.objects.filter(descripcion=info['descripcion'])
                if tipoalm_en_base:
                    tipoalm_en_base = 'Tipo de almacenaje ' + info['descripcion'] + ' ya se encuentra dada de alta'
                    return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':tipoalm_en_base})
                tipoalm = TipoAlm(
                    descripcion = info['descripcion']
                    )
                tipoalm.save()
                grabado = 'Tipo de almacenaje ' + tipoalm.descripcion + ' creado exitosamente.'
                return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':grabado})
            else:
                grabado = 'Formulario invalido'
                return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm, 'msj':grabado})
        #boton para crear tipo alm
        
        
        else:
            
            return redirect('index')
    return render(request,'operaciones/parametros.html',{'formcia':formcia, 'formcatub':formcatub, 'formpack': formpack, 'formcatrepo':formcatrepo, 'formcatpk': formcatpk, 'formtipoalm':formtipoalm})
    
    
@login_required
def nuevo_aforo(request):
    
    
    if request.method == 'POST':
        form_crear_producto = FormCrearProducto(request.POST)
        if form_crear_producto.is_valid():

            informacion = form_crear_producto.cleaned_data
            
            validar_cia = informacion['cia']
            cia_en_base = Cia.objects.filter(cod=validar_cia)
            
            if cia_en_base:
                
                peso_caja = float(informacion['peso_un']) * float(informacion['unidad_caja'])
                
                peso_pallet = float(informacion['peso_un']) * float(informacion['unidad_pall'])
                
                user = request.user
                
                producto = Producto(cia = informacion['cia'],
                                codigo = informacion['codigo'],
                                descripcion = informacion['descripcion'],
                                peso_un = informacion['peso_un'],
                                largo_un = informacion['largo_un'],
                                ancho_un = informacion['ancho_un'],
                                alto_un = informacion['peso_un'],
                                unidad_caja = informacion['unidad_caja'],
                                largo_cj = informacion['peso_un'],
                                ancho_cj = informacion['ancho_cj'],
                                alto_cj = informacion['alto_cj'],
                                unidad_pall = informacion['unidad_pall'],
                                usuario = user,
                                pack = informacion['pack'],
                                vd = informacion['vd'],
                                tipo_alm = informacion['tipo_alm'],
                                cat_ub = 'UB',
                                cat_pk = 'pk',
                                cat_repo = 'rep',
                                cat_emb = '001',
                                clase = 'B',
                                unidad_minima = 1 ,
                                unidad_medida = '01',
                                fecha_creacion = datetime.now(),
                                )
                producto.peso_cj = peso_caja
                producto.peso_pall = peso_pallet
                producto.largo_pall = '1,2'
                producto.ancho_pall = '1'
                producto.alto_pall = '1,4'
                producto.importado_saad = 'No'
                producto.importado_presis = 'No'
                producto.save()
                
                form_crear_producto = FormCrearProducto(informacion)
                form_creado = 'Cod ' + producto.codigo + ' creado exitosamente'
                return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, 'form2':form_creado})
                # return redirect('nuevo_aforo')
            else:
                form_crear_producto = FormCrearProducto(informacion)
                form_error = 'La CIA no existe, verifique...'
            return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, 'form2':form_error} )
        else:
            form_crear_producto = FormCrearProducto()
        return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto})
    form_crear_producto = FormCrearProducto()
    return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto})

@login_required
def exportar_saad(request):
    export = []
    productos = Producto.objects.filter(importado_saad='No')
    
    export.append([
        'Cia',
        'Producto',
        'Descripcion',
        'Clase',
        'Unidad_min',
        'peso_un',
        'largo_un',
        'ancho_un',
        'alto_un',
        'unid_medida',
        'cant_cj',
        'peso_cj',
        'largo_cj',
        'ancho_cj',
        'alto_cj',
        'cant_pall',
        'peso_pall',
        'largo_pall',
        'ancho_pall',
        'alto_pall',
        'cat_ub',
        'cat_pk',
        'cat_repo',
        'cat_emb',
        'rubro',
        'subrubro',
        'lote',
        'serie',
        'tip_serie',
        'desc_fant',
        'cod_barra_1',
        'cod_barra_2',
        'cod_barra_3',
        'ref A',
        'ref B',
        'cant_dias_vto',
        'fecha_elab',
    ])
    
    for producto in productos:
        producto.importado_saad = 'Si'
        
        producto.save()
        export.append([
            producto.cia,
            producto.codigo,
            producto.descripcion,
            producto.clase,
            producto.unidad_minima,
            producto.peso_un,
            producto.largo_un,
            producto.ancho_un,
            producto.alto_un,
            producto.unidad_medida,
            producto.unidad_caja,
            producto.peso_cj,
            producto.largo_cj,
            producto.ancho_cj,
            producto.alto_cj,
            producto.unidad_pall,
            producto.peso_pall,
            producto.largo_pall,
            producto.ancho_pall,
            producto.alto_pall,
            producto.cat_ub,
            producto.cat_pk,
            producto.cat_repo,
            producto.cat_emb,
            producto.pack,
            '',
            '',
            '',
            '',
            producto.descripcion,
            '',
            '',
            '',
            '',
            '',
            '',
            ''  
    ])
    hoy = datetime.now()
    strHoy = hoy.strftime("%Y%m%d")
    sheet = excel.pe.Sheet(export)
    return excel.make_response(sheet, "xlsx", file_name="Alta SAAD"+ strHoy + ".xlsx")


@login_required
def exportar_presis(request):
    export = []
    productos = Producto.objects.filter(importado_presis='No')
    
    export.append([
        'Cia',
        'Producto',
        'Descripcion',
        'Clase',
        'Unidad_min',
        'peso_un',
        'largo_un',
        'ancho_un',
        'alto_un',
        'unid_medida',
        'cant_cj',
        'peso_cj',
        'largo_cj',
        'ancho_cj',
        'alto_cj',
        'cant_pall',
        'peso_pall',
        'largo_pall',
        'ancho_pall',
        'alto_pall',
        'cat_ub',
        'cat_pk',
        'cat_repo',
        'cat_emb',
        'rubro',
        'subrubro',
        'lote',
        'serie',
        'tip_serie',
        'desc_fant',
        'cod_barra_1',
        'cod_barra_2',
        'cod_barra_3',
        'ref A',
        'ref B',
        'cant_dias_vto',
        'fecha_elab',
    ])
    
    for producto in productos:
        producto.importado_presis = 'Si'
        
        
        export.append([
            producto.cia,
            producto.codigo,
            producto.descripcion,
            producto.clase,
            producto.unidad_minima,
            producto.peso_un,
            producto.largo_un,
            producto.ancho_un,
            producto.alto_un,
            producto.unidad_medida,
            producto.unidad_caja,
            producto.peso_cj,
            producto.largo_cj,
            producto.ancho_cj,
            producto.alto_cj,
            producto.unidad_pall,
            producto.peso_pall,
            producto.largo_pall,
            producto.ancho_pall,
            producto.alto_pall,
            producto.cat_ub,
            producto.cat_pk,
            producto.cat_repo,
            producto.cat_emb,
            producto.pack,
            '',
            '',
            '',
            '',
            producto.descripcion,
            '',
            '',
            '',
            '',
            '',
            '',
            ''  
    ])
        producto.save()
    hoy = datetime.now()
    strHoy = hoy.strftime("%Y%m%d")
    sheet = excel.pe.Sheet(export)
    return excel.make_response(sheet, "xlsx", file_name="Alta PRESIS"+ strHoy + ".xlsx")

    

def ver_productos(request):
    id_producto = request.GET.get('codigo')
    #productos_listado = Producto.objects.all()
    
    if id_producto:
        productos_listado = Producto.objects.filter(codigo=id_producto)
        
    else:
        productos_listado = Producto.objects.all().order_by('-id')
        form = FormBusquedaProducto()
    
    form = FormBusquedaProducto()
    return render(request, 'operaciones/ver_productos.html', {'form':form,'productos_listado':productos_listado} )

@login_required
def editar_producto(request, id):
    prod = Producto.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormEditarProducto(request.POST)
        if form.is_valid():
            prod.cia = form.cleaned_data.get('cia')
            prod.codigo = form.cleaned_data.get('codigo')
            prod.descripcion = form.cleaned_data.get('descripcion')
            prod.peso_un = form.cleaned_data.get('peso_un')
            prod.largo_un = form.cleaned_data.get('largo_un')
            prod.ancho_un = form.cleaned_data.get('ancho_un')
            prod.alto_un = form.cleaned_data.get('alto_un')
            prod.unidad_caja = form.cleaned_data.get('unidad_caja')
            prod.largo_cj = form.cleaned_data.get('largo_cj')
            prod.ancho_cj = form.cleaned_data.get('ancho_cj')
            prod.alto_cj = form.cleaned_data.get('alto_cj')
            prod.unidad_pall = form.cleaned_data.get('unidad_pall')
            prod.pack = form.cleaned_data.get('pack')
            prod.vd = form.cleaned_data.get('vd')
            prod.tipo_alm = form.cleaned_data.get('tipo_alm')
            
            datos = form.cleaned_data
            if form.cleaned_data.get('peso_un') and form.cleaned_data.get('unidad_caja') and form.cleaned_data.get('unidad_pall'):
                peso_caja = float(datos['peso_un']) * float(datos['unidad_caja'])
                peso_pallet = float(datos['peso_un']) * float(datos['unidad_pall'])
                prod.peso_cj = peso_caja
                prod.peso_pall = peso_pallet
            
            prod.importado_saad = 'No'
            prod.importado_presis = 'No'
            prod.save()
            return redirect('ver_productos')
        
        else:
            return render(request, 'operaciones/editar_producto.html', {'form': form, 'producto':prod})

    form_producto = FormEditarProducto(initial={
        'cia': prod.cia,
        'codigo': prod.codigo,
        'descripcion': prod.descripcion,
        'peso_un': prod.peso_un, 
        'largo_un': prod.largo_un,
        'ancho_un': prod.ancho_un,
        'alto_un': prod.alto_un, 
        'unidad_caja': prod.unidad_caja, 
        'largo_cj': prod.largo_cj, 
        'ancho_cj': prod.ancho_cj, 
        'alto_cj': prod.alto_cj, 
        'unidad_pall': prod.unidad_pall, 
        'pack': prod.pack, 
        'vd': prod.vd, 
        'tipo_alm': prod.tipo_alm, 
        
        })
    return render(request, 'operaciones/editar_producto.html', {'form':form_producto, 'producto':prod})

@login_required
def index_deposito(request):
    return render(request, 'operaciones/index_operaciones.html')
from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from operaciones.forms import FormCrearProducto
from datetime import datetime
from operaciones.models import Cia, Producto
import django_excel as excel

from django.contrib.auth.decorators import login_required



# Create your views here.
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
                                
                                pack = informacion['pack'],
                                
                                vd = informacion['vd'],
                                que_es = informacion['que_es'],
                                usuario = 'SANTU',
                                cat_ub = 'UB',
                                cat_pk = 'pk',
                                cat_repo = 'repo',
                                cat_emb = 'emb',
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
                producto.importado = 'No'
                producto.save()
                
                form_crear_producto = FormCrearProducto(informacion)
                form_creado = 'Cod ' + producto.codigo + ' creado exitosamente'
                return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, 'form2':form_creado})
                # return redirect('nuevo_aforo')
            else:
                form_crear_producto = FormCrearProducto(informacion)
                form_error = 'CIA no existente'
            return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, 'form2':form_error} )
        else:
            form_crear_producto = FormCrearProducto()
        return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto})
    form_crear_producto = FormCrearProducto()
    return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto})

@login_required
def exportar_saad(request):
    export = []
    productos = Producto.objects.filter(importado='No')
    
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
        producto.importado = 'Si'
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



class CrearCia(LoginRequiredMixin, CreateView):
    model = Cia
    template_name = 'operaciones/nueva_cia.html'
    success_url = '/operaciones/crear_cia'
    fields = ['cod', 'descripcion']
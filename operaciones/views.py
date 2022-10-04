from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from operaciones.forms import FormCrearProducto
from datetime import datetime
from operaciones.models import Producto
import django_excel as asd

# Create your views here.

def nuevo_aforo(request):
    if request.method == 'POST':
        form_crear_producto = FormCrearProducto(request.POST)
        if form_crear_producto.is_valid():
            informacion = form_crear_producto.cleaned_data
            peso_caja = float(informacion['peso_un']) * float(informacion['unidad_caja'])
            # print(peso_caja)
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
            producto.save()
            
            return redirect('nuevo_aforo')
    else:
        form_crear_producto = FormCrearProducto()
    
    return render(request,'operaciones/nuevo_aforo.html',{'form':form_crear_producto, } )


def exportar_saad(request):
    pass
    
    
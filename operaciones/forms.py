from django import forms

class FormCrearProducto(forms.Form):
    cia =  forms.CharField(max_length=3)
    codigo = forms.CharField(max_length=15)
    descripcion = forms.CharField(max_length=180)
    peso_un = forms.FloatField()
    largo_un = forms.FloatField()
    ancho_un = forms.FloatField()
    alto_un = forms.FloatField()
    unidad_caja = forms.IntegerField()
    largo_cj = forms.FloatField()
    ancho_cj = forms.FloatField()
    alto_cj = forms.FloatField()
    unidad_pall = forms.IntegerField()
    pack = forms.CharField(max_length=15)
    vd = forms.FloatField()
    que_es = forms.CharField(max_length=15)
    
    
    
class FormBusquedaProducto(forms.Form):
    codigo = forms.CharField(max_length=15)
    
    
    
class FormEliminarProducto(forms.Form):
    codigo = forms.CharField(max_length=15)
    
    
class FormEditarProducto(forms.Form):
    cia =  forms.CharField(max_length=3)
    codigo = forms.CharField(max_length=15)
    descripcion = forms.CharField(max_length=180)
    peso_un = forms.FloatField()
    largo_un = forms.FloatField()
    ancho_un = forms.FloatField()
    alto_un = forms.FloatField()
    unidad_caja = forms.IntegerField()
    largo_cj = forms.FloatField()
    ancho_cj = forms.FloatField()
    alto_cj = forms.FloatField()
    unidad_pall = forms.IntegerField()
    pack = forms.CharField(max_length=15)
    vd = forms.FloatField()
    que_es = forms.CharField(max_length=15)
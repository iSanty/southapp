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
    tipo_alm = forms.CharField(max_length=15)
    
    
    
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
    tipo_alm = forms.CharField(max_length=15)
    
    
class FormCrearCia(forms.Form):
    cod = forms.CharField(max_length=3)
    descripcion = forms.CharField(max_length=180)
    
class FormCrearCatUb(forms.Form):
    cod = forms.CharField(max_length=3)
    descripcion = forms.CharField(max_length=180)
    
class FormCatPk(forms.Form):
    cod = forms.CharField(max_length=3)
    descripcion = forms.CharField(max_length=180)
    
class FormCatRepo(forms.Form):
    cod = forms.CharField(max_length=3)
    descripcion = forms.CharField(max_length=180)
    
class FormTipoAlm(forms.Form):
    descripcion = forms.CharField(max_length=180)
    
class FormPack(forms.Form):
    descripcion = forms.CharField(max_length=10)
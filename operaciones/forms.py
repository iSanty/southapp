from django import forms

from operaciones.models import Cia, TipoPack, TipoAlm

class FormCrearProducto(forms.Form):
    cia =  forms.ModelChoiceField(queryset= Cia.objects.all())
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
    pack = forms.ModelChoiceField(queryset= TipoPack.objects.all())
    vd = forms.FloatField()
    tipo_alm = forms.ModelChoiceField(queryset= TipoAlm.objects.all())
    
    
    
class FormBusquedaProducto(forms.Form):
    codigo = forms.CharField(max_length=15)
    
    
    
class FormEliminarProducto(forms.Form):
    codigo = forms.CharField(max_length=15)
    
    
class FormEditarProducto(forms.Form):
    cia =  forms.ModelChoiceField(queryset= Cia.objects.all())
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
    pack = forms.ModelChoiceField(queryset= TipoPack.objects.all())
    vd = forms.FloatField()
    tipo_alm = forms.ModelChoiceField(queryset= TipoAlm.objects.all())
    
    
class FormCrearCia(forms.Form):
    cod = forms.CharField(max_length=3)
    descripcion = forms.CharField(max_length=180)
    
class FormCrearCatUb(forms.Form):
    cia_asociada = forms.ModelChoiceField(queryset=Cia.objects.all())
    cod = forms.CharField(max_length=3)
    descripcion = forms.CharField(max_length=180)

class FormCrearCatUbVal(forms.Form):
    cia_asociada = forms.ModelChoiceField(queryset=Cia.objects.all())
    cod = forms.CharField(max_length=3)
    descripcion = forms.CharField(max_length=180)
    
class FormCatPk(forms.Form):
    cia_asociada = forms.ModelChoiceField(queryset=Cia.objects.all())
    cod = forms.CharField(max_length=3)
    descripcion = forms.CharField(max_length=180)
    
class FormCatRepo(forms.Form):
    cia_asociada = forms.ModelChoiceField(queryset=Cia.objects.all())
    cod = forms.CharField(max_length=3)
    descripcion = forms.CharField(max_length=180)
    
class FormTipoAlm(forms.Form):
    descripcion = forms.CharField(max_length=180)
    
class FormPack(forms.Form):
    descripcion = forms.CharField(max_length=10)
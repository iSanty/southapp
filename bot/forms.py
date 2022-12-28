from django import forms
from ckeditor.fields import RichTextFormField


class frmMensajePorEstado(forms.Form):
    estado = forms.CharField()
    mensaje = RichTextFormField()
    
    
    
class frmConsultaEstado(forms.Form):
    nro_guia = forms.CharField()
    
    
class frmMailParaElBot(forms.Form):
    mail = forms.EmailField()
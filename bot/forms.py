from django import forms
from ckeditor.fields import RichTextFormField


class frmMensajePorEstado(forms.Form):
    estado = forms.CharField()
    mensaje = RichTextFormField()
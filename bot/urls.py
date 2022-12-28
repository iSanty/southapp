from django.urls import path
from .views import bot, crear_mensaje_por_estado, edicion_mensaje, consultar_estado, mail_bot



urlpatterns = [
    path('', bot),
    path('mensajes_por_estado/', crear_mensaje_por_estado, name='mensajes_por_estado'),
    path('edicion_mensaje/<int:id>/', edicion_mensaje, name='edicion_mensaje'),
    path('consultar_estado/', consultar_estado, name='consultar_estado'),
    path('mail_bot/', mail_bot, name='mail_bot'),


]


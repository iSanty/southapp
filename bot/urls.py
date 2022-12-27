from django.urls import path
from .views import bot, crear_mensaje_por_estado



urlpatterns = [
    path('', bot),
    path('mensajes_por_estado/', crear_mensaje_por_estado, name='mensajes_por_estado'),
    


]


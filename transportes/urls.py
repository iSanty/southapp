from django.urls import path
from . import views

urlpatterns = [
    path('', views.CrearTransporte.as_view(), name='index_transporte'),
    #path('crear_transporte', views.CrearTransporte.as_view(), name='crear_transporte'),



]

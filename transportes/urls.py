from django.urls import path
from . import views

urlpatterns = [
    path('', views.mandarafreirchurros, name='index_transporte'),
    path('busqueda_transporte/', views.VerTransporte.as_view(), name='busqueda_transporte'),
    path('ver_dominio/<dominio>/', views.ver_dominio , name = 'ver_dominio'),



]


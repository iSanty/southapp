from django.urls import path
from . import views

urlpatterns = [
    path('', views.CrearTransporte.as_view(), name='index_transporte'),
    path('busqueda_transporte', views.VerTransporte.as_view(), name='busqueda_transporte'),
    path('ver_dominio/<int:pk>/', views.VerDominio.as_view() , name = 'ver_dominio'),



]

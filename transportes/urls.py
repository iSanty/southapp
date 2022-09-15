from django.urls import path
from . import views

urlpatterns = [
    path('', views.CrearTransporte.as_view(), name='CrearTransporte'),



]

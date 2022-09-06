from django.urls import path
from .views import index_empleados

urlpatterns = [
    path('', index_empleados, name='index_empleados'),



]

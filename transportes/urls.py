from django.urls import path
from .views import index_transportes

urlpatterns = [
    path('', index_transportes, name='index_transportes'),



]

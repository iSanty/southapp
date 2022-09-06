from django.urls import path
from .views import index_informes


urlpatterns = [
    
    
    path('', index_informes, name='index_informes'),



]

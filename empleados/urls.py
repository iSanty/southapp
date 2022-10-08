from django.urls import path
from .views import index_meli, linkeo

urlpatterns = [
    
    path('', linkeo, name='linkeo'),
    
    path('meli/', index_meli, name='index_meli'),

]


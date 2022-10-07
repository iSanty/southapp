from django.urls import path
from .views import index_meli

urlpatterns = [
    path('meli/', index_meli, name='index_meli'),

]

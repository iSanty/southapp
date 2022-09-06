from django.urls import path
from .views import index_accounts

urlpatterns = [
    path('', index_accounts, name='index_accounts'),



]

"""SouthApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index, error, documentacion
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('404/', error, name='404'),
    path('transportes/', include('transportes.urls')),
    path('empleados/', include('empleados.urls')),
    path('accounts/', include('accounts.urls')),
    path('informes/', include('informes.urls')),
    path('operaciones/', include('operaciones.urls')),
    path('api/', include('api.urls')),
    path('bot/', include('bot.urls')),
    path('inicio/', include('pagina.urls')),
    path('webhooks/', include('webhooks.urls')),
    path('documentacion/', documentacion, name="documentacion")
    

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
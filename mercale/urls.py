"""mercale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from patrimonial.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', countOS, name='inicio'),
    path('os/', os, name='os'),
    path('equipamentos/', equipamentos, name='equipamentos'),
    path('prestador/', prestador, name='prestador'),
    path('marcas/', marcas, name='marcas'),
    path('modelo/', modelo, name='modelo'),
    path('cadastraros', cadastroos, name='cadastraros'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('nova_os/', cadastroos, name='cadastrar_os'),
    path('add_marca/', add_marca, name='add_marca'),
    path('aguardando/', aguardandoOS, name='aguardando'),


]

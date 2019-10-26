from django.contrib import admin

from django.contrib import admin
from .models import *

admin.site.register(Equipamento)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Os)
admin.site.register(Prestador_servico)
from django.shortcuts import render
from patrimonial.models import *

def index(request):
    os = Os.objects.all()
    return render(request, 'index.html', locals())

def equipamentos(request):
    equipamento = Equipamento.objects.all()
    return render(request, 'equipamentos.html', locals())

def prestador(request):
    prestador = Prestador_servico.objects.all()
    return render(request, 'prestador.html', locals())

def marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'marcas.html', locals())

def modelo(request):
    modelo = Modelo.objects.all()
    return render(request, 'modelos.html', locals())
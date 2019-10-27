from django.shortcuts import render, redirect
from patrimonial.models import *
from .forms import OsForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


@login_required
def index(request):
    os = Os.objects.all().order_by('-dt_saida')
    countos = Os.objects.all().count()
    return render(request, 'index.html', locals())

@login_required
def countOS(request):
    countos = Os.objects.all().count()
    return render(request, 'contador.html', locals())

@login_required
def equipamentos(request):
    equipamento = Equipamento.objects.all()
    return render(request, 'equipamentos.html', locals())


@login_required
def prestador(request):
    prestador = Prestador_servico.objects.all()
    return render(request, 'prestador.html', locals())


@login_required
def marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'marcas.html', locals())


def modelo(request):
    modelo = Modelo.objects.all()
    return render(request, 'modelos.html', locals())

@login_required
def login(request):
    if request.method =='POST':
        user = authenticate(username=request.POST['usarname'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/equipamentos')
    return render(request, 'registration/../templates/base_login.html')


def cadastroos(request):
    if request.method == 'POST':
        form = OsForm(request.POST)
        if form.is_valid():
            osform = form.save()
            osform.save()
            return redirect('/')
    form = OsForm()
    return render(request, 'cadastraros.html', {'form' : form})


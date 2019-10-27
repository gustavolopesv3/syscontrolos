from django.shortcuts import render, redirect
from patrimonial.models import *
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Sum


@login_required
def index(request):
    contar = Os.objects.all().count()
    return render(request, 'base.html', locals())

def os(request):
    os = Os.objects.all().order_by('-dt_saida')
    return render(request, 'os.html', locals())

@login_required
def countOS(request):
    countos = Os.objects.all().count()
    aguardando = Os.objects.filter(dt_retorno=None).count()
    equipamento = Equipamento.objects.all().count()
    gastos = Os.objects.aggregate(valor_servico=Sum('valor_servico')).get('valor_servico')
    return render(request, 'base.html', locals())

@login_required
def aguardandoOS(request):
    aguardando = Os.objects.filter(dt_retorno=None)
    return render(request, 'aguardando.html', locals())

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
    return render(request, 'registration/login.html')


def cadastroos(request):
    if request.method == 'POST':
        form = OsForm(request.POST)
        if form.is_valid():
            osform = form.save()
            osform.save()
            return redirect('/')
    form = OsForm()
    return render(request, 'cadastraros.html', {'form' : form})

def add_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            marcaform = form.save()
            marcaform.save()
            return redirect('/')
    form = MarcaForm()
    return render(request, 'add_marca.html', {'form' : form})
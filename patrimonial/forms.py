from django import forms
from django.forms import ModelForm
from .models import *

class OsForm(forms.ModelForm):
    class Meta:
        model = Os
        fields = ('motivo','ns', 'dt_saida', 'dt_retorno', 'descricao', 'servico_executado','resposavel_interno' , 'resposavel_empresa', 'valor_servico', 'empresa')

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('nome',)
from django import forms

from .models import Os

class OsForm(forms.ModelForm):
    class Meta:
        model = Os
        fields = ('motivo','ns', 'dt_saida', 'dt_retorno', 'descricao', 'servico_executado','resposavel_interno' , 'resposavel_empresa', 'valor_servico', 'empresa')
        widgets = {
            'motivo' : forms.TextInput(),
            'ns' : forms.TextInput(),
            'dt_saida' : forms.DateField,
            'dt_retorno' : forms.DateField,

        }
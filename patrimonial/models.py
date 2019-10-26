from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Modelo(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    descricao = models.CharField('Descrição',max_length=50)
    numero_serie = models.CharField('Numero de Serie', max_length=30)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_serie

class Prestador_servico(models.Model):
    cnpj = models.IntegerField('CNPJ')
    razao_social = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=20)
    cep = models.IntegerField('CEP')
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.razao_social

class Os(models.Model):
    motivo = models.CharField(max_length=30)
    ns = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    dt_saida = models.DateField('Data de Saida')
    dt_retorno = models.DateField('Data de Retorno')
    descricao = models.TextField(max_length=200)
    servico_executado = models.CharField(max_length=50)
    resposavel_interno = models.CharField(max_length=50)
    resposavel_empresa = models.CharField(max_length=50)
    valor_servico = models.IntegerField()
    empresa = models.ForeignKey(Prestador_servico, on_delete=models.CASCADE)

    def __str__(self):
        return self.motivo


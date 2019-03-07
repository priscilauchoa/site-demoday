from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome_fantasia = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    CNPJ = models.IntegerField()
    descricao_da_empresa = models.CharField(max_length=200)
    porte_da_empresa = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.IntegerField()
    email = models.EmailField(max_length=100)
    site = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descricao_da_vaga = models.CharField(max_length=300)
    requisitos = models.CharField(max_length=100)
    carga_horaria = models.CharField(max_length=100)
    beneficios = models.CharField(max_length=100)
    local_de_trabalho = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_fantasia

from django.db import models
from django.utils import timezone

class Candidato(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.IntegerField()
    celular = models.IntegerField()
    email = models.EmailField()
    endereco = models.CharField(max_length=80)
    experiencia_prof = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome





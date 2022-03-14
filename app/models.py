from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class Endereco(models.Model):
    rua = models.CharField(max_length=60, null=False, blank=False)
    cidade = models.CharField(max_length=60, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=STATE_CHOICES)


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    endereco = models.ForeignKey(Endereco, null=True, on_delete=models.SET_NULL, related_name='clientes')
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    profissao = models.CharField(max_length=60, null=False, blank=False)

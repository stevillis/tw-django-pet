import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.br.br_states import STATE_CHOICES

CARGO_VETERINARIO_CHOICE = 1
CARGO_FINANCEIRO_CHOICE = 2
CARGO_ATENDIMENTO_CHOICE = 3
CARGO_CHOICES = (
    (CARGO_VETERINARIO_CHOICE, 'Veterinário'),
    (CARGO_FINANCEIRO_CHOICE, 'Financeiro'),
    (CARGO_ATENDIMENTO_CHOICE, 'Atendimento'),
)


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Endereco(BaseModel):
    rua = models.CharField(max_length=60, null=False, blank=False)
    cidade = models.CharField(max_length=60, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=STATE_CHOICES)


class Cliente(BaseModel):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    endereco = models.ForeignKey(Endereco, null=True, on_delete=models.SET_NULL, related_name='clientes')
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    profissao = models.CharField(max_length=60, null=False, blank=False)


class Pet(BaseModel):
    CATEGORIA_PET_CHOICES = (
        ('Ca', 'Cachorro'),
        ('Ga', 'Gato'),
        ('Co', 'Coelho'),
    )

    COR_PET_CHOICES = (
        ('Pr', 'Preto'),
        ('Br', 'Branco'),
        ('Ci', 'Cinza'),
        ('Ma', 'Marrom'),
    )

    nome = models.CharField(max_length=30, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    categoria = models.CharField(max_length=2, choices=CATEGORIA_PET_CHOICES, null=False, blank=False)
    cor = models.CharField(max_length=2, choices=COR_PET_CHOICES, null=False, blank=False)
    dono = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, blank=False, related_name='pets')


class Consulta(BaseModel):
    motivo = models.CharField(max_length=200, null=False, blank=False)
    peso_atual = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=3)
    medicacao_atual = models.TextField(null=False, blank=True)
    medicacao_prescrita = models.TextField(null=False, blank=True)
    exames_prescritos = models.TextField(null=False, blank=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        ordering = ['-created']


class Funcionario(AbstractUser):
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False, default=datetime.date.today())
    cargo = models.IntegerField(choices=CARGO_CHOICES, null=False, blank=False, default=CARGO_ATENDIMENTO_CHOICE)

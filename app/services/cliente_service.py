from typing import Union

from django.db.models import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404

from app.models import Cliente


def cadastrar_cliente(cliente: Cliente):
    Cliente.objects.create(
        nome=cliente.nome,
        email=cliente.email,
        cpf=cliente.cpf,
        data_nascimento=cliente.data_nascimento,
        profissao=cliente.profissao,
        endereco=cliente.endereco
    )


def listar_clientes() -> QuerySet:
    return Cliente.objects.all()


def listar_cliente_id(pk: int) -> Union[Cliente, Http404]:
    return get_object_or_404(Cliente, pk=pk)

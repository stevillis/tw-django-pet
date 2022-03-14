from typing import Union

from django.db.models import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404

from app.entidades.cliente import Cliente as ClienteObject
from app.models import Cliente as ClienteModel


def cadastrar_cliente(cliente: ClienteModel):
    ClienteModel.objects.create(
        nome=cliente.nome,
        email=cliente.email,
        cpf=cliente.cpf,
        data_nascimento=cliente.data_nascimento,
        profissao=cliente.profissao,
        endereco=cliente.endereco
    )


def listar_clientes() -> QuerySet:
    return ClienteModel.objects.all()


def listar_cliente_id(pk: int) -> Union[ClienteModel, Http404]:
    return get_object_or_404(ClienteModel, pk=pk)


def editar_cliente(cliente_antigo: ClienteModel, cliente_novo: ClienteObject):
    cliente_antigo.nome = cliente_novo.nome
    cliente_antigo.email = cliente_novo.email
    cliente_antigo.endereco = cliente_novo.endereco
    cliente_antigo.cpf = cliente_novo.cpf
    cliente_antigo.data_nascimento = cliente_novo.data_nascimento
    cliente_antigo.profissao = cliente_novo.profissao
    cliente_antigo.save(force_update=True)

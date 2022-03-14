from typing import Union

from django.http import Http404
from django.shortcuts import get_object_or_404

from app.entidades.endereco import Endereco as EnderecoObject
from app.models import Endereco as EnderecoModel


def cadastrar_endereco(endereco: EnderecoModel) -> EnderecoModel:
    return EnderecoModel.objects.create(rua=endereco.rua, cidade=endereco.cidade, estado=endereco.estado)


def listar_endereco_id(pk: int) -> Union[EnderecoModel, Http404]:
    return get_object_or_404(EnderecoModel, pk=pk)


def editar_endereco(endereco_antigo: EnderecoModel, endereco_novo: EnderecoObject) -> EnderecoModel:
    endereco_antigo.rua = endereco_novo.rua
    endereco_antigo.cidade = endereco_novo.cidade
    endereco_antigo.estado = endereco_novo.estado
    endereco_antigo.save(force_update=True)
    return endereco_antigo


def excluir_endereco(endereco: EnderecoModel):
    endereco.delete()

from typing import Union

from django.db.models import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404

from app.entidades.pet import Pet as PetObject
from app.models import Cliente as ClienteModel
from app.models import Pet as PetModel


def cadastrar_pet(pet: PetModel):
    PetModel.objects.create(
        nome=pet.nome,
        data_nascimento=pet.data_nascimento,
        categoria=pet.categoria,
        cor=pet.cor,
        dono=pet.dono
    )


def listar_pet_id(pk: int) -> Union[PetModel, Http404]:
    return get_object_or_404(PetModel, pk=pk)


def listar_pets_por_dono(dono: ClienteModel) -> QuerySet[PetModel]:
    return PetModel.objects.filter(dono=dono).all()


def editar_pet(pet_antigo: PetModel, pet_novo: PetObject):
    pet_antigo.nome = pet_novo.nome
    pet_antigo.data_nascimento = pet_novo.data_nascimento
    pet_antigo.dono = pet_novo.dono
    pet_antigo.categoria = pet_novo.categoria
    pet_antigo.cor = pet_novo.cor
    pet_antigo.save(force_update=True)

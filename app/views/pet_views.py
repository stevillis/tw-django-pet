from typing import Tuple

from django.shortcuts import redirect, render

from app.entidades import pet
from app.forms import pet_forms
from app.forms.pet_forms import PetForm
from app.services import cliente_service, pet_service


def get_pet_cleaned_data(form_pet: PetForm) -> Tuple:
    nome = form_pet.cleaned_data.get('nome')
    data_nascimento = form_pet.cleaned_data.get('data_nascimento')
    categoria = form_pet.cleaned_data.get('categoria')
    cor = form_pet.cleaned_data.get('cor')
    dono = form_pet.cleaned_data.get('dono')

    return nome, data_nascimento, categoria, cor, dono


def cadastrar_pet(request, cliente_id):
    dono_bd = cliente_service.listar_cliente_id(cliente_id)
    if request.method == 'POST':
        form_pet = pet_forms.PetForm(request.POST)

        if form_pet.is_valid():
            nome, data_nascimento, categoria, cor, _ = get_pet_cleaned_data(form_pet)

            pet_novo = pet.Pet(nome=nome, data_nascimento=data_nascimento, categoria=categoria, cor=cor, dono=dono_bd)
            pet_service.cadastrar_pet(pet_novo)

            return redirect('listar-clientes')
    else:
        form_pet = pet_forms.PetForm()
    context = {
        'form_pet': form_pet,
        'dono': dono_bd.nome,
        'is_edit': False
    }
    return render(request, 'pets/form_pet.html', context)


def listar_pet_id(request, pk):
    pet_bd = pet_service.listar_pet_id(pk)
    return render(request, 'pets/lista_pet.html', {'pet': pet_bd})


def editar_pet(request, pk):
    pet_antigo = pet_service.listar_pet_id(pk)
    form_pet = pet_forms.PetForm(request.POST or None, instance=pet_antigo)
    if form_pet.is_valid():
        nome, data_nascimento, categoria, cor, dono = get_pet_cleaned_data(form_pet)
        pet_novo = pet.Pet(nome=nome, data_nascimento=data_nascimento, categoria=categoria, cor=cor, dono=dono)

        pet_service, editar_pet(pet_antigo, pet_novo)
        return redirect('listar-clientes')
    context = {
        'form_pet': form_pet,
        'is_edit': True
    }
    return render(request, 'pets/form_pet.html', context)

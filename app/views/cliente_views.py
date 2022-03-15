from typing import Tuple

from django.shortcuts import redirect, render

from app.entidades import cliente, endereco
from app.forms.cliente_forms import ClienteForm
from app.forms.endereco_forms import EnderecoForm
from app.services import cliente_service, endereco_service, pet_service


def get_cliente_cleaned_data(form_cliente: ClienteForm) -> Tuple:
    nome = form_cliente.cleaned_data.get('nome')
    email = form_cliente.cleaned_data.get('email')
    cpf = form_cliente.cleaned_data.get('cpf')
    data_nascimento = form_cliente.cleaned_data.get('data_nascimento')
    profissao = form_cliente.cleaned_data.get('profissao')

    return nome, email, cpf, data_nascimento, profissao


def get_endereco_cleaned_data(form_endereco: EnderecoForm) -> Tuple:
    rua = form_endereco.cleaned_data.get('rua')
    cidade = form_endereco.cleaned_data.get('cidade')
    estado = form_endereco.cleaned_data.get('estado')

    return rua, cidade, estado


def listar_clientes(request):
    clientes = cliente_service.listar_clientes()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def listar_cliente_id(request, pk):
    cliente_bd = cliente_service.listar_cliente_id(pk)
    pets = pet_service.listar_pets_por_dono(cliente_bd)
    context = {
        'cliente': cliente_bd,
        'pets': pets
    }
    return render(request, 'clientes/lista_cliente.html', context)


def cadastrar_cliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoForm(request.POST)

        if form_cliente.is_valid():
            nome, email, cpf, data_nascimento, profissao = get_cliente_cleaned_data(form_cliente)

            if form_endereco.is_valid():
                rua, cidade, estado = get_endereco_cleaned_data(form_endereco)

                endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)

                cliente_novo = cliente.Cliente(nome=nome, email=email, cpf=cpf, data_nascimento=data_nascimento,
                                               profissao=profissao, endereco=endereco_bd)
                cliente_service.cadastrar_cliente(cliente_novo)

                return redirect('listar-clientes')
    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoForm()

    context = {
        'form_cliente': form_cliente,
        'form_endereco': form_endereco,
        'is_edit': False
    }
    return render(request, 'clientes/form_cliente.html', context)


def editar_cliente(request, pk):
    cliente_editar = cliente_service.listar_cliente_id(pk)
    form_cliente = ClienteForm(request.POST or None, instance=cliente_editar)

    endereco_editar = endereco_service.listar_endereco_id(cliente_editar.endereco.pk)
    form_endereco = EnderecoForm(request.POST or None, instance=endereco_editar)

    if form_cliente.is_valid():
        nome, email, cpf, data_nascimento, profissao = get_cliente_cleaned_data(form_cliente)

        if form_endereco.is_valid():
            rua, cidade, estado = get_endereco_cleaned_data(form_endereco)

            endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
            endereco_editado = endereco_service.editar_endereco(cliente_editar.endereco, endereco_novo)

            cliente_novo = cliente.Cliente(nome=nome, email=email, cpf=cpf, data_nascimento=data_nascimento,
                                           profissao=profissao, endereco=endereco_editado)
            cliente_service.editar_cliente(cliente_editar, cliente_novo)

            return redirect('listar-clientes')

    context = {
        'form_cliente': form_cliente,
        'form_endereco': form_endereco,
        'is_edit': True
    }
    return render(request, 'clientes/form_cliente.html', context)


def excluir_cliente(request, pk):
    cliente_bd = cliente_service.listar_cliente_id(pk)
    endereco_bd = endereco_service.listar_endereco_id(pk)
    if request.method == 'POST':
        cliente_service.excluir_cliente(cliente_bd)
        endereco_service.excluir_endereco(endereco_bd)
        return redirect('listar-clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente_bd})

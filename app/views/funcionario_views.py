from typing import Tuple

from django.shortcuts import redirect, render

from app.entidades import funcionario
from app.forms.funcionario_forms import FuncionarioForm
from app.services import funcionario_service


def get_funcionario_cleaned_data(form_funcionario: FuncionarioForm) -> Tuple:
    nome = form_funcionario.cleaned_data.get('nome')
    data_nascimento = form_funcionario.cleaned_data.get('data_nascimento')
    cargo = form_funcionario.cleaned_data.get('cargo')

    return nome, data_nascimento, cargo


def listar_funcionarios(request):
    funcionarios = funcionario_service.listar_funcionarios()
    return render(request, 'funcionarios/lista_funcionarios.html', {'funcionarios': funcionarios})


def cadastrar_funcionario(request):
    if request.method == 'POST':
        form_funcionario = FuncionarioForm(request.POST)

        if form_funcionario.is_valid():
            nome, data_nascimento, cargo = get_funcionario_cleaned_data(form_funcionario)
            funcionario_novo = funcionario.Funcionario(nome=nome, data_nascimento=data_nascimento, cargo=cargo)

            funcionario_service.cadastrar_funcionario(funcionario_novo)
            return redirect('listar-funcionarios')
    else:
        form_funcionario = FuncionarioForm()

    context = {
        'form_funcionario': form_funcionario,
        'is_edit': False
    }
    return render(request, 'funcionarios/form_funcionario.html', context)
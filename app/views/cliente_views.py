from django.shortcuts import render

from app.entidades import cliente, endereco
from app.forms.cliente_forms import ClienteForm
from app.forms.endereco_forms import EnderecoForm
from app.services import cliente_service, endereco_service


def cadastrar_cliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoForm(request.POST)

        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data.get('nome')
            email = form_cliente.cleaned_data.get('email')
            cpf = form_cliente.cleaned_data.get('cpf')
            data_nascimento = form_cliente.cleaned_data.get('data_nascimento')
            profissao = form_cliente.cleaned_data.get('profissao')

            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data.get('rua')
                cidade = form_endereco.cleaned_data.get('cidade')
                estado = form_endereco.cleaned_data.get('estado')

                endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)

                cliente_novo = cliente.Cliente(nome=nome, email=email, cpf=cpf, data_nascimento=data_nascimento,
                                               profissao=profissao, endereco=endereco_bd)
                cliente_service.cadastrar_cliente(cliente_novo)
    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoForm()
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})

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

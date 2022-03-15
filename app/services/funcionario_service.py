from app.models import Funcionario


def listar_funcionarios() -> Funcionario:
    return Funcionario.objects.all()


def cadastrar_funcionario(funcionario):
    Funcionario.objects.create(nome=funcionario.nome, data_nascimento=funcionario.data_nascimento,
                               cargo=funcionario.cargo)

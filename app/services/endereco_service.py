from app.models import Endereco


def cadastrar_endereco(endereco: Endereco) -> Endereco:
    return Endereco.objects.create(rua=endereco.rua, cidade=endereco.cidade, estado=endereco.estado)

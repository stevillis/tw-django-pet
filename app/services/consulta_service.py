from django.db.models import QuerySet

from app.entidades.consulta import Consulta as ConsultaObject
from app.models import Cliente as ClienteModel
from app.models import Consulta as ConsultaModel
from app.models import Pet as PetModel


def cadastrar_consulta(consulta: ConsultaObject):
    ConsultaModel.objects.create(
        motivo=consulta.motivo,
        peso_atual=consulta.peso_atual,
        medicacao_atual=consulta.medicacao_atual,
        medicacao_prescrita=consulta.medicacao_prescrita,
        exames_prescritos=consulta.exames_prescritos,
        pet=consulta.pet
    )


def listar_consultas_por_pet(pet: PetModel) -> QuerySet[ConsultaModel]:
    return ConsultaModel.objects.filter(pet=pet).all()


def listar_consultas_por_dono(dono: ClienteModel) -> QuerySet[ConsultaModel]:
    return ConsultaModel.objects.filter(pet__dono=dono).all()


def listar_consulta_por_id(pk: int) -> ConsultaModel:
    return ConsultaModel.objects.get(pk=pk)

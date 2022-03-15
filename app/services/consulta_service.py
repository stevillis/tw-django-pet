from app.entidades.consulta import Consulta as ConsultaObject
from app.models import Consulta as ConsultaModel


def cadastrar_consulta(consulta: ConsultaObject):
    ConsultaModel.objects.create(
        motivo=consulta.motivo,
        peso_atual=consulta.peso_atual,
        medicacao_atual=consulta.medicacao_atual,
        medicacao_prescrita=consulta.medicacao_prescrita,
        exames_prescritos=consulta.exames_prescritos,
        pet=consulta.pet
    )

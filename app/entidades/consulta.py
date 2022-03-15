class Consulta:
    def __init__(self, motivo, peso_atual, medicacao_atual, medicacao_prescrita, exames_prescritos, pet):
        self.__motivo = motivo
        self.__peso_atual = peso_atual
        self.__medicacao_atual = medicacao_atual
        self.__medicacao_prescrita = medicacao_prescrita
        self.__exames_prescritos = exames_prescritos
        self.__pet = pet

    @property
    def motivo(self):
        return self.__motivo

    @motivo.setter
    def motivo(self, motivo):
        self.__motivo = motivo

    @property
    def peso_atual(self):
        return self.__peso_atual

    @peso_atual.setter
    def peso_atual(self, peso_atual):
        self.__peso_atual = peso_atual

    @property
    def medicacao_atual(self):
        return self.__medicacao_atual

    @medicacao_atual.setter
    def medicacao_atual(self, medicacao_atual):
        self.__medicacao_atual = medicacao_atual

    @property
    def medicacao_prescrita(self):
        return self.__medicacao_prescrita

    @medicacao_prescrita.setter
    def medicacao_prescrita(self, medicacao_prescrita):
        self.__medicacao_prescrita = medicacao_prescrita

    @property
    def exames_prescritos(self):
        return self.__exames_prescritos

    @exames_prescritos.setter
    def exames_prescritos(self, exames_prescritos):
        self.__exames_prescritos = exames_prescritos

    @property
    def pet(self):
        return self.__pet

    @pet.setter
    def pet(self, pet):
        self.__pet = pet

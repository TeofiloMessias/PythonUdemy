class Robo:

    def __init__(self, nome, bateria=100, habilidade=[]):
        self.__nome = nome
        self.bateria = bateria
        self.habilidade = habilidade

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidade(self):
        return self.__habilidade

    @property
    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'BEEP BOOP BEEP BOOP, EU SOU {self.__nome.upper()}'
        return 'Bateria fraca. Por favor, recarregue e tente novamente'

    def aprender_habilidade(self, nova_habilidade, custo):
        if self.__bateria >= custo:
            self.__bateria -= custo
            self.__habilidade.append(nova_habilidade)
            return f'Uau! EU APRENDI {nova_habilidade.upper()}'
        return 'Bateria insuficiente. Por favor, recarregue novamente'


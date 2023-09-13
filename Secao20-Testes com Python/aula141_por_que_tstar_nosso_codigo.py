"""
Po que testar nosso código?

Testes Automatizados!

        Aplicação web
----------------------------
|                           |
|   frontend e backend      |
----------------------------
|   testes automatizados    |
----------------------------

Po que testar nosso código?
    - Reduzir bugs (problemas) no código existente;
    - Testes garantem que novos recusrsos da sua aplicação não quebrem (alterem) recurso antigo;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriomente continuam corrigidos;
    - Testes garantem que a refatoração que costumamos a fazer não tragam novos bugs (problemas);

TDD - Test Driven Development (Desenvolvimeto Giado por Testes)

Com TDD é utilizado estagios de desenvolvimento:
    - Você escreve seu teste primeiro
    - Então você escreve o código minimo suficiente para fazer o teste passar ( ou seja, executar com sucesso);
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passse, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor
"""

class Gato:

    def __init__(self, nome):
        self.__nome = nome

    def miar(self):
        print(f'{self.__nome} esta miando...')

felix = Gato('Felix')

felix.miar()

print(felix.nome)
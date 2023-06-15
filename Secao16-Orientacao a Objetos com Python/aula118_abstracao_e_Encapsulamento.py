"""
POO - Abstração e encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo logico e hierárquico utiliando
classes.

Encampsular -> Cápsula

        classe
--------------------------------
|                               |
|       atributos e métodos     |
|-------------------------------|

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método privado
chamado __falar()

Esses elementos privados só devem/deveria ser acessados
dentro da classe. Mas Python não bloqueia este acesso
fora da classe. Com Python acontece um fenômeno chamado
Name mangling, que faz uma alteração na forma de se
acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementoos privados fora da classe:

instancia._Pessoas__nome

instancia._Pessoas__falar()

Abstração em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.

conta1 = Conta('Geek', 150.00, 1500)

# Depois de deixar tudo privado os dados abaixo deixam de fazer acesso
# print(conta1.numero)
# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)

# conta1.numero = 42
# conta1.titular = 'Xuxa'
# conta1.saldo = 9999999999999
# conta1.limite = 9999999999999999999999999

print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular) # Name Mangling

conta1._Conta__titular = 'Angelina'
print(conta1.__dict__)

# Testando

conta1 = Conta('Geek', 150.00, 1500)
print(conta1.__dict__)

conta1.depositar(150)
print(conta1.__dict__)

conta1.sacar(200)
print(conta1.__dict__)
"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo,limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta origem
        self.__saldo -= valor
        self.__saldo -= 10 # taxa de transferencia paga por quem realizou a transferencia

        # 2 - Adicionar o valor na conta destino
        conta_destino.__saldo += valor

conta1 = Conta('Angelina', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Felicity', 300, 2000)
conta2.extrato()

valor = 100

# conta2.sacar(valor)
# conta1.depositar(valor)
conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()
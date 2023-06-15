"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. ambém extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nos extendenmos outra class
que pass a herdar atributos e métodos da classe herdada

Cliente
    - nome;
    - sobremnome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobremnome;
    - cpf;
    - matricula;

Perguntar: Exite alguma entidade generica o suficiente para encapsular os atributos
e métodos comuns a outras entidades ?


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 500)
funcionario = Funcionario('Felicity', 'Jones', '987.654.321-11',123)


print(cliente1.nome_completo())
print(funcionario.nome_completo())

Qunado uma classe herda de outra classe ela herda todos os atributos e métodos da classe herdada.

Qunado uma classe herda de outra classe, a classe herdade é conhecida por:
    - Super Classe;
    - Classe mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica
Qunado uma classe herda de outr classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha
    - Classe Epsecifica;

class Pessoa:

    def __init__(self, nome, sobrenome,cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self,nome, sobrenome, cpf) # Forma não comum de acessar dados da super classe
        self.__renda = renda

class Funcionario(Pessoa):
    #Funcionário herda de Pessoa
    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)# Forma comum de acessar dados da super classe
        self.__matricula = matricula


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 500)
funcionario = Funcionario('Felicity', 'Jones', '987.654.321-11',1234)

print(cliente1.nome_completo())
print(funcionario.nome_completo())

print(cliente1.__dict__)
print(funcionario.__dict__)

# Sobrescrita de Métodos (Overrinding)

Sobrescrita de Método, ocorre qunado reescrevemos/reimplementamos ummétodo presente na super classe

"""

class Pessoa:

    def __init__(self, nome, sobrenome,cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self,nome, sobrenome, cpf) # Forma não comum de acessar dados da super classe
        self.__renda = renda

class Funcionario(Pessoa):
    #Funcionário herda de Pessoa
    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf) # Forma comum de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 500)
funcionario = Funcionario('Felicity', 'Jones', '987.654.321-11',1234)

print(cliente1.nome_completo())
print(funcionario.nome_completo())


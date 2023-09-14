"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de míltipla classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

# OBS: A herança múltipla pode ser deita de duas maneiras:
    - Por Multiderivação Direta
    - Por Multiderivação Indireta

    # Exemplo 1 - Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1,Base2,Base3):
    pass

# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass

#OBS: Não importa se a derivação é direta ou indireta. A classe que realiza a herença herdará
todos os atributos ew métodos das super classe.
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'Eu sou {self._Animal__nome} esta nadando. '

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar !'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando. '

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra! '

class Pinguim(Aquatico,Terrestre): # A oredem da erança afeta o metodo cumprimentar

    def __init__(self, nome):
        super().__init__(nome)

# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())
print('----------------------------------')

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())
print('----------------------------------')

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar()) # Method Resolution Order - MRO

# Objeto é instacia de...

print(f'Tux é instancia de Pinguim ? {isinstance(tux, Pinguim)}')   # True
print(f'Tux é instancia de Pinguim ? {isinstance(tux, Aquatico)}')  # True
print(f'Tux é instancia de Pinguim ? {isinstance(tux, Terrestre)}') # True
print(f'Tux é instancia de Pinguim ? {isinstance(tux, Animal)}')    # True
print(f'Tux é instancia de Pinguim ? {isinstance(tux, object)}')    # True
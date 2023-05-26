"""
Funções de Maior Grandeza - Higher order Functions - HOF

O que isso segnifica ?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
que retorna outras funções como resultado ou mesmo que podemos passar funções
como argumentos para putras funções, e até mesmo criar variáveis do tipo de funções
nos nosso programas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são Cidado~es de Primeira Classe, First Class Citizen.

# Exemplo - Definindo as funções

def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções

print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))


# nested Functions - Funções Aninhadas

#Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
# ou também Inner Functions ( Funções Internas


# Exemplo

from random import  choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

# Testando

print(cumprimento('Angelina'))

print(cumprimento('Felicity'))


# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahahahaha', 'kkkkkkk', 'yayayayayayaya'))
    return rir

# Testando
rindo = faz_me_rir()
print(rindo())

"""

# Inner Function ( Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas.


from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahaha', 'lololo','kkk'))
        return f'{risada} {pessoa}'
    return dando_risada()

# testando

rindo = faz_me_rir_novamente('Ferananda')

print(rindo)
print(rindo)
print(rindo)
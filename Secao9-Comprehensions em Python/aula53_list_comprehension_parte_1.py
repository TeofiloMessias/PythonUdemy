"""
List Comprehension - Parte 1

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro
interável.

# Sintaxe da List Comprehension

[ dado for dado in interavel ]

# Exemplos

numeros =[1,2,3,4,5]

res = [numeros * 10 for numeros in numeros]

print(res)

Para entender melhor o que esta acontecendo devemos dividir a expressa em duas parte:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10

res = [numeros / 2 for numeros in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numeros) for numeros in numeros]
print(res)

# List Comprehension

# loop
numeros_dobrados = []

for numeros in [1,2,3,4,5]:
    numeros_dobrados.append(numeros * 2)

print(numeros_dobrados)

# List Comprehension
print([numeros * 2 for numeros in [1,2,3,4,5]])
"""

# Outros exemplos

# 1


nome = 'Geek university'

print([letra.upper() for letra in nome])

# 2

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigos) for amigo in amigos])

# 3

print([numeros * 3 for numeros in range(1,10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(numeros) for numeros in [1,2,3,4,5]])
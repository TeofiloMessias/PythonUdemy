"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por pareênteses ().

2 - As tuplas são imutáveis: Isso significa que ao se criar tupla ela não muda. Toda
peração em um tupla gera uma nova tupla.

# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1,2,3,4,5,6)
print(tupla1)

print(type(tupla1))

tupla2 = 1,2,3,4,5,6
print(tupla2)

print(type(tupla1))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla!
print(tupla3)

print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla!
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do parenteses

(4) -> Não é tupla
(4,)-> É tupla
4, -> É tupla

#Podemos gerar uma tupla dinaicamente com range(inicio,fim,passo)
tupla =tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek University','Programação em Python: Essencial')

escola, curso = tupla
print(escola)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desenpacotar.

# Métodos para: adição e romoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis

# Sooma*, Valor Máximo*,Valor Mínimo* e Tamanho

# * Se os valores forem todos inteirosou reais

tupla = (1,2,3,4,5,6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1,2,3)
print(tupla1)

tupla2 = (4,5,6)
print(tupla1)

print(tupla1 + tupla2) # Tuplas são imutáveis

print(tupla1)
print(tupla1)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla1)

tupla1 = tupla1 + tupla2 # Tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = (1,2,3)

print(3 in tupla)

# Iterando sobre uma tupla
tupla = (1,2,3)

for n in tupla:
    print(n)

for indece,valor in enumerate(tupla):
    print(indece,valor)

# Contando elementos dentro de uma tupla

tupla = ('a','b','c','d','e','a','b')
print(tupla.count('a'))

escola = tupla('Geek University')

print(escola)
print(escola.count('e'))

    # Verificamos em qual índice um elemento está na tupla

print(meses.index('Junho'))

# OBS: Caso o elemento não exista, será gerado ValueError.

# Dias na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisamos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('janeiro', 'fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# slicing
#Tupla [ inicio: fim: passo ]

print(meses[5:9])

# O acesso a elementos de uma tupla é semelhante a de uma lista
print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Po que utilizar tupla ?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro*.

# * Isso poque trabalhar com elementos imutaveis traz segurança para o codigo
"""

# Copiando uma tuppla para outra

tupla = (1,2,3)
print(tupla)

nova = tupla # Na tupla não temops o problema de Shallow copy

print(nova)
print(tupla)

outra = (4,5,6)

nova = nova + outra
print(nova)
print(tupla)




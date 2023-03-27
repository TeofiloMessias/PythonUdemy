"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para interar sobre sequencia ou sobre valores interáveis

Exemplos de iteráveis:
 - Strings
       nome = 'Geek University'
 - Lista
       lista = [ 1, 3, 5, 7, 9]
 - Range
       numeros = range(1, 10)

nome = 'Geek University'
lista = [ 1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em um lista
    print(letra)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando em uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 2 (Iterando em uma range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
    print(numero)

Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descarta-lo utilizando um underline (_)

nome = 'Geek University'
lista = [ 1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em um lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar ?'))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'Imprimindo {qtd}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Tabela de emojis Unicode: https://timwhitlock.info/emoji/tables/unicode
                          https://unicode.org/emoji/charts/full-emoji-list.html
"""

# Original: U+1F60D
# Modificado: U0001F60D

for num in range(1, 11):
    print('U0001F60D' * num)









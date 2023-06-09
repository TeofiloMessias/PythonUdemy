"""
Listas

Listas em Pyton funcional como  vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICA e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e podera ter SEMPRE no máximo 5 valores.

Ja em Python:

- Dinãminco: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de daodo fixo; Ou seja podemos colocar qualquer tipo de dado;

As listas em Pyton são representadas por colchetes: []

Listas são mutáveis: Ou seja elas podem mudar constantemente.

type([])

lista1 = [1, 99, 4, 27, 15, 22 ,3, 1, 44, 42, 27]

lista2 = ['G','e','e','k',' ', 'U','n','i','v','e','r','s','i','t','y']

lista3 = []

lista = list(range(11))

lista5 = list('Geek University')

# Podemos falcilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o numero {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o numero de ocorrencia de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas


Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com append nos so conseguimos adicionar um elemento por vez
# lista.append(12, 34, 56) # Erro

lista1.append([8, 3, 1]) # Coloca a lista como elemento único (sublista)
print(lista1)

if [8,3,1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional á lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo Valor')
print(lista)

# Podemos facilmente juntar duas listas

#lista6 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[:: -1])
print(lista2[:: -1])

# Copiar uma lista
lista6 = lista2.copy()

# podemos contar quantos elementos  exitem dentro da lista
print(len(lista1))

# Podemos remover facilmente o ultimo elemento de uma lista
# OBS: O pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover o elemento pelo índice
# OBS: O elementos a direita deste índice serão deslocados para a esquerda
# OBS: Se não houver o elemento no índece informado, teremos o erro IndexError
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1,2,3]
print(nova)
nova = nova * 3
print(nova)

# podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python:','Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1,2.34, True, 'Geek', 'd',[1,2,3], 4534535345]
print(lista6)
print(type(lista6))

# Interando sobre listas

# Exemplo 1 - utilizando for

soma = 0
for elemento in lsita4
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print(" Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

        # Utilizando variáveis em lista
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#          0          1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para enteder o indice negativo pense na lista como um círculo, onde
# o final de um elemento esta ligado ao final da lista
print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
#print(cores[-5]) # Erro, pois não existe ídice -5

for cor in cores:
    print(cor)

indice = 0
while indice <len(cores):
    print(cores[indice])
    indice = indice + 1

cores = ['verde', 'amarelo', 'azul', 'branco']

# gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice,cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)

# Outros médotos não tão importante mas também úteis
# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice da lista está o valor 6?
print(numeros.index(6))

# Em qual índice da lista está o valor 9?
print(numeros.index(9))

# print(numeros.index(19)) # Gera ValueError
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

#OBS: Retorna o índice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5,1)) # buscando a partir do índice 1
print(numeros.index(5,2)) # buscando a partir do índice 2
print(numeros.index(5,3)) # buscando a partir do índice 3
# print(numeros.index(5,4)) # buscando a partir do índice 4
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8,3,6)) # Buscar o índice do valor 8, entre os indice 3 a 6

# Revisão de slicing

# lista[inicio:fim:passo
#range(inicio:fim:passo)

#trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes

#trabalhando com slice de lista com o parâmetro 'fim'

print(lista[:2]) # começa em 0, pega até o índice 2 - 1

print(lista[:4]) # começa em 0, pega até o índice 4 - 1

print(lista[1:3]) # começa em 1, pega até o índice 3 - 1

#trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2

print(lista[::2]) # Começa em 0, vai até o final, de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ['Geek', 'University']

nomes.reverse()
print(nomes)

# Soma, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

lista = [1,2,3,4,5,6]
print(sum(lista)) # Soma
print(max(lista)) # máximo valor
print(min(lista)) # mínimo valor
print(len(lista)) # tamanho da lista

# Transformar uma lista em tupla

lista = [1,2,3,4,5,6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1,2,3]
num1, num2,num3 = lista

print(num1)
print(num2)
print(num3)
# OBS: Se tivermos um numero diferente de elementos na lista ou variaveis para recebermos os dados, teremos ValueErro

# Copiaando uma list apara outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy
lista = [1,2,3]
print(lista)

nova = lista.copy() # Cópia

print(nova)

nova.append(4)

print(lista)
print(nova)


# Veja que utilizamos lista.copy copiamos os dados da lista para uma nova lista, mas elas
# focaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# é chamado de Deep Copy (cópia profunda)

"""

# Forma 2 - Shallow Copy

lista = [1,2,3]
print(lista)

nova = lista # Cópia
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamosos dados da lista para nova lista, mas
# após realizar modificação em uma das lista, essa modificação se refletiu em ambas as listas
# Isso em Python é chamado de Shallow Copy


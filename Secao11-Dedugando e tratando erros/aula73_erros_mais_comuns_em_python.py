"""
erros mias comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler saidas de erros geradas pela execução
do nosso código.

Os erros mais comuns:

1 - SyntaxError -> Ocorre qunado o Python encontra um erro de sintaxe.Ou seja, você escreveu algo que
o Python não reconhece como parte da linguagem

Exemplos SyntaxError

a)

def funcao:
    print('Geek university')

b)
def = 1

c)
return

2 - NameError -> Ocorre quando uma variável ou função não foi definida

Exemplos NameError

a)
print(geek)

b)
geek()

c)
a = 18
#para resolver
#msn = 'Não é menor que 10'
if a < 10:
    msn = 'É menor que 10'

print(msn)

3 - TypeError -> ocorre quando uma função/operação é aplicada a um tipo errado

Exemplos TypeError

a)
print(len(5))

b) print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido.

Exemplos  IndexError

a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[0][10])

c)
tupla = ('Geek')
print(tupla[0][10])

5 - ValueError -> ocorre quando uma função/operação built-in (integrada) recebe um argumetno com tipo correto
mas o valor inapropriado

# Exemplos  ValueError

a)
print(input('Geek')) convertendo uma string para inteiro

6 - KeyError -> ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos  KeyError

a)
dic = {}
print(dic['geek'])

7 - AttributeError -> ocorre quando uma variável não tem um atributo/função

# Exemplos  AttributeError

a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

8 - IndentationError -> Ocorre qunaod não respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError

a)

def nova():
print('Geek')

nova()

b)
for in range(10):
i + 1

print(i)

OBS: Exceptions e Erros são sinônimos na programação

OBS: Importante ler e prestar atenção na saida de erro.
"""








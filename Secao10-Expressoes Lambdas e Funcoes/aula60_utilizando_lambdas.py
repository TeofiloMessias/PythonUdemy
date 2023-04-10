"""
Utilizando Lambdas

Conhecidas por Expressoes Lambdas, ou seja simplesmente lambdas, são funções sem nome, ou seja,
funções anônimas.

# Funções em Python

def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

# Expressão Lambda
lambda x: 3 * x + 1

# E como utilizar a expressão lambda ?
cal = lambda x: 3 * x + 1
print(funcao(4))
print(funcao(7))

# strip() remove espaço no começo e no fim '  angelina '

# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome,sobrenome: nome.strip().title() + ' '+ sobrenome.strip().title()
print(nome_completo('    angelina ','JOLIE'))
print(nome_completo('FELICITY', 'jones'))

# Em funções Python podemos ter nunhuma ou várias entradas. Em lambdas também

amar = lambda: ' Como não amar Python ?'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3/(1/x + 1/y + 1 /z)

#n = lambda x1m x1, ..., xn <expressão>

print(amar)
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumentos do que parâmentos esperados teremos TypeError

# Outro exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert','Orson Scott Card',
           'Douglas Adams', 'H.G.Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
"""

# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """ Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
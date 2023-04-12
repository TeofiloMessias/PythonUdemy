"""
Len, Abs, Sum e Round

# Len

len() -> Retorna o tamanho (ou seja, onumero de itens) de um iterável.

# Só para revisar

print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len (dois underline)
print('Geek university'.__len__)

# Abs

abs() - > Retorna o valor absoluto de um numero inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

# Exemplos ABS

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Sum

sum() - Recebe como paramentro um iterável, podendo receber um valor inicial, e retornaa a soma dos elementos, incluindo o valor inicial
OBS: O valor inical default = 0

# Exemplos

print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.14, 5.678]))

print(sum((1, 2, 3, 4, 5)))

print(sum({1, 2, 3, 4, 5}))

print(sum({'a':1, 'b':2, 'c':3, 'd':4, 'e':5}.values()))

# Round

 round() -> Retorna um numero arrendodado para n digito de precisão após a casa decimal. Se a precisão não for
 informada retorna o inteiro mais próximo da entrada.
"""


# Exemplo Round

print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1.2121212121, 2))

print(round(1.21999999, 2))


"""
Módulo Collections - Counter (Contador)

https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-performace Container Datetypes

Counter -> Recebe um interavel como parâmentro e cria um objeto do tipo Collections Couter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmento e como valor a quantidade
de ocorrências desse elemento.

# Podemos utilizar qualquer iterável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(lista))

print(res)

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Geek University'))
"""

# Realizando o import

from collections import Counter

# Exemplo 3

texto = """Max Heindel, nascido Carl Louis Fredrik Graßhoff 
(Aarhus, Dinamarca; 23 de Julho de 1865 — Oceanside, Califórnia, 
6 de Janeiro de 1919), foi um ocultista, astrólogo e místico cristão
dinamarquês de origem alemã, radicado nos Estados Unidos. 
Entre os estudantes dos seus ensinamentos é reconhecido 
como o maior místico do século XX no ocidente."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 mais palavras com mais ocorr~encia no texto
print(res.most_common(5))

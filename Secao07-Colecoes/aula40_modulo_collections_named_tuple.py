"""
Módulo Collections  - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

# recap tupla
tupla =(1, 2, 3)

print(tupl[1])

Named Tuple -> São tupla, diferenciadas, onde, especificamente um nome para a mesma e também
"""
# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmentros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade', 'raca', 'nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

# Acessando os dados

# Forma 1

print(ray[0]) # idade
print(ray[1]) # raça
print(ray[2]) # nome

# Forma 2

print(ray.idade) # idade
print(ray.raca) # raça
print(ray.nome) # nome

print(ray.index('Chow-Chow')) #Qual o idece
print(ray.count('Chow-Chow')) # Qunatas ocorrencia

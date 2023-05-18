"""
Módulo Collections - Deque

podemos dizer que o deque é uma lista de alta performace.
"""

# Importa
from collections import deque

# Criando deques

deq = deque('geek')

# Adicionando elementos no deque

deq.append('y') # Adiciona no final
print(deq)

deq.append('k') # Adiciona no começo
print(deq)

# Remover elementos

print(dep.pop()) #Remove e retorna o ultimo elemento
print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento
print(deq)
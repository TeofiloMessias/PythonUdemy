"""
Módulo Collection - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# recp Dicionários

dicionarios = {'curso': 'Programação em Python: Essencial'}

print(dicionarios)

print(dicionarios['curso'])

print(dicionarios['outro']) # ??? KeyError

Default Dic -> Ao criar um dicionario utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Esta valor será utilizado sempre que não houver
um valor definido. Caso tentemos acesssar uma chave que não exista, essa chave será
criada e o valor default será atribuido.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar valores
"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro']) # KeyError no dicionário comum, mas aqui não.

print(dicionario)



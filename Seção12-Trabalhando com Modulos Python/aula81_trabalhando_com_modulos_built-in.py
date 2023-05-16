"""
Trabalahando com Módulos Built-in (módulos integrados, que ja vem instalados no Pytho

________________________
|Python|Módulos builtin|
------------------------

# Utilizando alis (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())

# Importando todo o módulo

import random

print(random.random())

# Utilizando alis (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5,89))
print(rdm)

https://docs.python.org/3/py-modindex.html
"""

# Costumamos a utilizar tuple para colocar multiplos imports de um mesmo modulo
from random import (
    random,
    randint,
    shuffle,
    choice
)
print(random())

print(randint(3,7))

lista = ['Geek', 'University','Python']
shuffle(lista)
print(lista)

print(choice('University'))




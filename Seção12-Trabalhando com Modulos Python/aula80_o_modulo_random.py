"""
Módulo Random e o que são módulos?

- Em python, modulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo (não recomendado).

import random

# random() -> Gera um numero real pseudo-aleatório entre 0 e 1

# OBS: Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# debtro do módulo ficarão disponíveis (Ficarão em Memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2.

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função,
# separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função randon() e
# apenas uma função dentro do módulo randon.

# Forma 2 - Importando uma função especifica do módulo (Forma Recomendada)

from random import random

# No import acima, estamos falando: Do módulo random, iporte a função random

for i in range(10):
    print(random())


# uniform() -> Gerar um número real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3,7)) # 7 não é incluido

# randint() -> gera valores pseudo-aleatórios entre os valores estabelecidos
from random import randint
# Gerador de aposta para mega-sena
for i in range(6):
    print(randint(1,61), end=', ') # começa em 1 e vai até 60

# choice() -> Mostra um valor aleatório entre um iteravel

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
print(choice('GeekUniversity')

"""
from random import shuffle
# shufle() -> Tem a função de embaralhar dados

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)

shuffle(cartas)
print(cartas.pop())  # entrega uma carta




"""
Abra um terminal com python3.7
Abra um terminal com python3.8


>>>import collections
>>>from timeit import timeit

>>>Pessoa = collection.namedtuple('pessoa', 'nome email')

>>>felicity = Pessoa('Felicity Jones', 'felicity@gmail.com')

print(timeit('felicity.email', globals=globals()))

# globals() é uma função
"""
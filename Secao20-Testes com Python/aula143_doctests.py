"""
Doctests

Doctests são testes que colocamos na docstring  funções/métodos Python.

Para rodar um test do doctest:

python - m doctest -v nome_do_modulo.py

# SAÍDA

Trying:
    soma(1,2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
    1 tests in doctests.soma
1 tests in 2 items.
1 passes and 0 failed.
Test passed.

# EXEMPLO
def soma(a,b):
    (""Colocar aspas"")soma os numeros a e b
    (>>>)soma(1, 3)
    3

    (>>>) soma(4, 6)
    10
    (""Colocar aspas"")
return a + b

# EXEMPLO

# Outro Exemplo, Aplicando TDD

def duplicar(valores):
    #duplicar os valores em uma lista

    #>>> duplicar([1, 2, 3, 4])
   # [2, 4, 6, 8]

    #>>> duplicar([])
    #[]

   #>>> duplicar(['a', 'b', 'c'])
    #['aa', 'bb', 'cc']

  #>>> duplicar([True, None])
   # Traceback (most recent call last):
    #    ...
   # TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
   #
   # return [2 * elemento for elemento in valores]

# EXEMPLO

# Erro inesperado

OBS: Dentro do doctests, o Python não reconhece string com aspas duplas. Precisa ser aspas simples

def fala_oi():
    # colocar aspas
   # >>> fala_oi()
    'oi'
    # colocar aspas
    #return "oi"

# EXEMPLO

"""

# Um ultimo caso estranho...

def verdade():
    """
    Retorna verdade

    >>> verdade()
    True
    """
    return True

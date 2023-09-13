"""
Introdução ao módulo Unittest

Unittest -> Teste Unitários

O que são testes unitários?

Teste é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser : funções, métodos, classes módulos etc.

OBS: Teste unitário não é especifico da Linguagem Python.

para criar nosos testes, criamos classe sque herdam de unittest. TestCase
e a partir de então ganhamos os 'assertion' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Caso de teste para sua unidade

# Conhecendo as assetions

https://docs.python.org/3/library/unittest.html

Método                          Checa que
assertEqual(a, b)               a == b
assertNotEqual(a, b)            a != b
assertTrue(x)                   x é verdadeiro
assertFalse(x)                  x é falso
assertIs(a, b)                  a é b
assertIsNot(a, b)               a não é b
assertIfNone(x)                 x é None
assertIsNotNone(x)              x não é none
assertIn(a, b)                  a esta em b
assertNotIn(a, b)               a não esta em b
assertIsInstance(a, b)          a é instância de b
assertNotIsInstance(a, b)       a não é instância de b

Por convenção, todos os testes em um test case, deve ter seu nome
inicado com underline

Para executar os testes com unittest

pyton nome_do_modulo.py

# Para executar os testes com unittest no modo verboso

python nome_do_modulo - v

# Docstring nos testes

Podemos acrescentar (e é recomendado) docstrings nos nosso testes.
"""
# Prática - utilizando a abordagem TDD


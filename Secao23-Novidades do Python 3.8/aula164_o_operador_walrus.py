"""
O operador Walrus permite fazer a atribuição e retorno de valores em uma única expressão

variavel := expressão
"""

# nome = 'Geek University'
#
# print(nome)
#
# print(nome := 'Geek University')

# Python 3.7
# cesta = []
# fruta = input('Informe o nome da fruta: ')
# while fruta != 'jaca':
#     cesta.append(fruta)
#     fruta = input('Infrome a fruta: ')

# Python 3.8
cesta = []
while(fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)
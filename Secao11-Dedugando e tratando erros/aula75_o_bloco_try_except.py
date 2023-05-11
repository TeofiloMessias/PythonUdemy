"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrerno nosso código. Previnindo
assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral masi simples é:

try:
    //execução problematica
except:
    // o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico
try:
    geek()
except:
    print('Deu algum problema aqui')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

# Exemplo 2 - Tratando um erro genérico
try:
    len(5)
except:
    print('Deu algum problema aqui')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erro. O ideal é SEMPRE
tratar de forma específica.

# Exemplo 3 Tratando um erro especifico

try:
    geek()
except NameError:
    print('Você esta utilizando uma função inexistente')

# Exemplo 4 Tratando um erro especifico

try:
    len(5)
except TypeError:
    print('Você esta utilizando uma função inexistente')

# Exemplo 5 Tratando um erro especifico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Exemplo 5 Tratando um erro especifico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez

try:
    #len(5)
    #geek()
    #print('Geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')

# Podemos efetuar diversos tratamentos de erros de uma vez

try:
    print('Geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')
"""

def pega_valor(dicionario,chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'Geek'}
print(pega_valor(dic,'nome'))

# print(pega_valor(dic,8)) -> TypeError






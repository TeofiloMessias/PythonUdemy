"""
Try / Except / Else / Finally

Dica de quando e onde tratar código

TODA ENTRADA DEVE SER TRATADA

OBS: A função do usu

# else  -> É executado somente se não ocorrer o erro.

try:
    nun = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Voce digitou {nun}')

# Finally

try:
    num = int(input('Informe um número'))
except ValueError:
    print('Voce não digitou um valor válido')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é SEMPRE executado. Independente se houver exceção ou não.

# O finally, geralmente, é utilizado para fechaar ou desalocar recursos.

# Exemplo mais complexo ERRADO

def dividir(a,b):
    return a/b

num1 = int(input('Informe o primeiro número:'))
try:
    num2 = int(input('Informe o segundo número:'))
except ValueError:
    print('O valor precisa ser númerico')

try:
    print(dividir(num1,num2))
except NameError:
    print('Valor incorreto')


# Exemplo mais complexo CORRETO
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a,b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1,num2))

# Exemplo mais complexo - GENERICO
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a,b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'



num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1,num2))
"""

# Exemplo mais complexo - Semi Generico
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a,b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError)as err:
        return f'Valor incorreto {err}'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1,num2))


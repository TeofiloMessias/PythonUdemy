"""
Assertions (Afirmações/Checagens/Questionamentos

Em Python utilizamos a palavra reservada ' assert' para realizar simples
afirmações utilizadas nos testes

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retona None e caso seja flasa levanta um erro
do tipo AssertionError.

# OBS: Nós podemos especificar, opcionalmente, um segundo arqumento ou mesmo uma mensagem de erro personalizada

# OBS: A palavra 'assert' pode ser utilizada em qulaquer função ou código nosso...não precisa
ser exclusivamente nos testes.
"""
def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b

retorno = soma_numeros_positivos(2,4) # 6

retorno soma_numeros_positivos(-2, 4) # AssertionError
print(retorno)

def comer_fast_food(comida)
    assert comida in [
        'pizza',
        'sorvete'
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f' Eu estou comendo {comida}'

comida = input('Informe a comida: ')
print(comer_fast_food(comida))

# ALERTA: Cuidado ao utilizar ' assert'

def faca_algo_ruim(usuario):
    assert usuario.eh_admin, ' Somente administradores podem fazer coisas ruim! '
    destroi_todo_o_sistema()
    return 'Adeus'

# caso você abra o terminal do python e execute o comando dessa maneira
# python -O + nome do seu arquivo.py o sitema não valida os erros que você esta validando
# no seu assert
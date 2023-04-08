"""
Funções com parãmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função

def quadrado(numero): # recebendo um parametro
    #return numero * numero
    return  numero ** 2
print(quadrado(7)) # argumento passado foi 7
print(quadrado(2))
print(quadrado(5))

# podemos tambem fazer usando uma variavel
ret = quadrado(6)
print(ret)

# print(quadrado()) # TypeError

# Refatorando uma função

def cantar_parabens(aniversariante):
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')

cantar_parabens('Marcos')

# Funções podem ter n parametros de entrada. Ou seja, podemos receber como entrada
# em uma função quantos paramentros forem necessários. Eles são separados por virgula.


def soma(a,b): #parametro de entrada (a e b)
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2,5)) # argumentos (os valores)
print(soma(10,20))

print(multiplica(2,5))
print(multiplica(2,8))

print(outra(3,2, 'Geek '))
print(outra(5,4, 'Python '))

# OBS: Se a gente informar um numero errado de parametros ou argumentos, temos TypeError.

# print(soma(2,3,4)) # TypeError - Passando argumentos a mais
# print(soma(4)) # TypeError - passando argumentos a menos

# Nomeando parametros

def nome_completo(nome,sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

# A diferença entre Parãmetros e Argumentos

# Parãmentos são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parametros importa !

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (key Arguments)

# Caso utilizamos nomes dos paramentros nos argumentos para informá-lo, podemos
#utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome,sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='marcia'))

"""
# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
            # return total -> fechando o return aqui esta errado, o correto é fechar no for e não no if
        return total
lista = [1,2,3,4,5,6,7]
print(soma_impares(lista))

tupla = (1,2,3,4,5,6,7)
print(soma_impares(tupla))

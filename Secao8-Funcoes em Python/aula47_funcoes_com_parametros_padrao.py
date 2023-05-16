"""
Funções com Parãmetros Padrão (Default Paramters)
 - Função onde a passagem de parãmetros seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')
print()

# Exemplo de função onde a passagem de parãmentro seja obrigatória
def quadrado(numero):
    return numero**2

print(quadrado(3))
print(quadrado()) # TypeError

def exponencial(numero=4, potencia=2): # se colocar um valor padrão no paramentro, esse valor passa a valer caso o usuario não coloque
    return numero ** potencia

print(exponencial(2,3)) # 2 * 2 * 2 = 8
print(exponencial(3,2)) # 3 * 3 = 8

print(exponencial(3)) # Por padrão eleve ao quadrado
print(exponencial(3,5)) # Eleva a potencia informada pelo usuário

# OBS: Se o usuario passar somente 1 argumento, este será atribuido ao parametro, e será calculado o quadrado deste numero;
# Se o usuário pasar 2 argumentos, o primerio serpa atribuido ao parametro numero e o segundo ao parametro potencia.Então
# será calculada esta potencia

print(exponencial())

# OBS: Em funções Python, os parametros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# ERRO!
def teste(num=2,potencia):
    return num ** potencia

print(teste(6))

def soma(num1,num2):
    return num1 + num2

print(soma(4,3))
print(soma(4)) # TypeError
print(soma()) # TypeError

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo istrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

# Por que utilizar parãmetros com valor default ?

- Nos permite ser mais flexiveis nas funções;
- Evita erros com parãmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código

# Quais tipos de dados podemos utilizar como valores default para parãmentros

- Qualquer tipo de dado:
    - números, strings,float,booleanos,lista,tuplas,dicionarios,funções e etc;

    # Exemplos
def soma(num1, num2):
    return num1 + num2

def mat(num1,num2,fun=soma()):
    return fun(num1,num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2,3))
print(mat(2,2,subtracao))

# Escopo - Evitar problemas e confusões...

# Variaveis globais
# Variaveis locais

instrutor = 'Geek' # Variavel global

def diz_oi():
    intrutor = 'Python' # Variavel local
    return f'Oi {instrutor}'

print(diz_oi())

# se tivermos uma variavel local com o mesmo nome de ua variavel global, a local terá preferencia

def diz_oi():
    prof = 'Geek' # Variável local
    return f' Olá {prof}'

print(diz_oi())

print(prof) # NameError

# ATENÇÃO com variaveis globais ( se puder evitar, evite! )

total = 0

def incrementa():
    total = total +1 # UnboundlocalError ( A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incrementa())


total = 0

def incrementa():
    global total # Avisando que queremos utilizar a variável global

    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())

"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

# print(dentro)  # Não é reconhecida ( NamedError )


"""
Decorators com Diferentes Assinaturas

# Para resolver, utilizamos um padrão de projeto chamado Decorator Patter

# Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def suadacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

# testando

#print(suadacao('Angelina'))

print(ordenar('Picanha','batat Frita'))

A assinatura de uma função é representada pelo seu retorno, nome e parametro de entrada.



# Refatorando com a Decorator Patter

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args,**kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

@gritar
def ordernar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

print(saudacao('Felicity'))

print(ordernar('Picanha', 'Batata Frita'))

@gritar
def lol():
    return 'lol'

print(lol())
"""

# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# Testando

print(soma_dez(10,11)) # 22

print(soma_dez(1,21)) # 22

print(comida_favorita('pizza', 'churrasco'))

print(comida_favorita('sanduiche', 'churrasco'))

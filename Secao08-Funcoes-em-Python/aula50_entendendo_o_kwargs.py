"""
**Kwargs

Poderiamos chamar este parãmetro de **xis, mas por convenção chamamos de **Kwargs

Este é só mais um parametro,mas diferente do *args que coloca os valores extra
em uma tupla, o **Kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parãmetros extras em um dicionário.
# Exemplo

def cores_favorita(**Kwargs):
    for pessoa, cor in Kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favorita(marcos='verde', julia='amarelo', fernanda='azul',venessa='branco')

# OBS: Os parãmetros *agrs e **Kargs não são obrigatórios.

cores_favorita()

cores_favorita(geek='navy')

# Exemplo mais compplexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek']=='Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

Nas nossas funções, podemos ter (NESTA ORDEM):
 - Parametros obrigatorios;
 - *args;
 - Paramentros default (não obrigatórios);
 - **kwargs

 def minha_funcao(idade,nome,*args,solteiro=False,**kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
        print(kwargs)

minha_funcao(8,'Julia')
minha_funcao(18,'Felicity',4,5,3,solteiro=True)
minha_funcao(34,'Felipe',eu='Não',voce='Vai')
minha_funcao(19,'Carla',9,4,3, java=False,python=True)

# Função com a ordem correta de parametros
#def mostra_info(a,b,*args, instrutor='Geek',**kwargs):
#    return [a,b,args,instrutor,kwargs]

# Função com a ordem incorreta de paramentos
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

a = 1
b = 2
args =(3,)
intrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}

print(mostra_info(1,2,3,sobrenome='University',cargo='Instrutor'))

# Desempacotr com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))
"""

def soma_multiplos_numeros(a,b,c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

# OBS! Os nomes da chave em um dicionário devem ser os mesmo dos paramnetros da função

#dicionario = dict(d=1, e=2, f=3) # TypeError
#soma_multiplos_numeros(**dicionario)

soma_multiplos_numeros(**dicionario, lang='Python')

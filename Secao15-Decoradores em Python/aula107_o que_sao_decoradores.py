"""
Decoradores ( Decoretors)

O que são decorators?

- Decoratos são funções
- Decorators envolvem outras funções e aprimoram seus comportamento
- Decoratos também são exmplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Sybtact Sugar / Açúcar Sintático)


|----------------------------------------------------|
|                 Function Decorator                 |
------------------------------------------------------

------------------------------------------------------
||---------------------------------------------------||
||                  Função decorada                  ||
||----------------------------------------------------|
|------------------------------------------------------

# Decoratos como função (Sintaxe não recomendada / Sem Açúcar Sintático)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem vindo(a) a Geek university')

# Testando 1

# saudacao()

teste = seja_educado(saudacao)

teste()

# Testando 2

def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)

raiva_educada()

# Decoratos com Syntac Sugar ( Açúcar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo()

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

# testando
apresentando

@seja_educado_mesmo
def dormir():
    print('Quero dormir...')

dormir
"""
"""
|-----------------------------------------------------------
|   Home    | Serviços  |   Produtos    |   Administrativo |
------------------------------------------------------------

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/servicos

http://www.suaempresa.com.br/produtos

http://www.suaempresa.com.br/login

# OBS: Não é código funcional ( Que funcione) é apenas exemplo

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br/login')


def home(request):
    return 'Pode acessar home'


@checa_login
def servicos(request):
    return 'Pode acessar servicos'


def produtos(request):
    return 'Pode acessar produtos'


@checa_login
def admim(request):
    return 'Pode acessar admim'

"""

# OBS: Não confunda Decorator com Decorator Function
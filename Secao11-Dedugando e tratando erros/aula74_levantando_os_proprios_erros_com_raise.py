"""
levantando os próprios erros com raise

raise -> lança exceções

OBS: O raise não é ima função. É uma palavra reservada , assi como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo util para que possamos criar nossas proprias exceções e mensagens
de erro.

A forma geral de utilização é:

raise TipoDoErro("Mensagem de erro')

# Exemplo real
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será improsso na {cor}')

#colore('Geek', 'azul')
colore('Geek', 1)

# Exemplo refatorado
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre:{cores}')
    print(f'O texto {texto} será improsso na {cor}')

colore('Geek University', 'preto')

OBS:

"""

# Exemplo refatorado
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre:{cores}')
    print(f'O texto {texto} será impresso na {cor}')

colore('Geek University', 'preto')

"""
Documentando funções com Docstrings

OBS: Podemos ter acesso a documentação de uma função em Python
utilizando a propriedade especila __do__

Podemos ainda fazer acesso a documentaação com a função help()

"""

def diz_oi():
    """Uma função simples que retorna a string 'Oi'"""
    return 'Oi!'

def exponencial(numero, potencial=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potenci' informada
    :param numero: Numero que desejamos gerar o exponencial.
    :param potencia: Potencia que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o exponencial de 'numero' por 'potencial'
    """
    return numero ** numero

"""
from docstrings import exponencial
exponencial.__doc__
    ou
help(exponencial)
"""

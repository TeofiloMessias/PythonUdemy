"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa
ter permissão:
    - Permissão de Leitura -> Para ler o arquivo
    - Permissão de Escrita -> Para escrever o arquivo

StringIO -> Utilizando para ler e criar arquivos em memória.
"""

# Primeiro fazemos o import
from io import StringIO

mensagem = 'este é apenas uma string normal'

# podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois

arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que ja sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write('Outro texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
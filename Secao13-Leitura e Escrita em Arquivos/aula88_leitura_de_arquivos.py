"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro
de entrada, que neste caso pe o caminho para o arquivo a ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/libraly/functions.html#open

OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
mode r -> MOde de Leitura. r -> read() -> Ler

"""

arquivo = open('texto.txt')

#print(arquivo)

#print(type(arquivo))

# para ler o contudeido de um arquivo após a sua abertura, devemos utilizar a função read()

ret = arquivo.read()
print(type(ret))
print(ret)

print(arquivo.read())

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado curso. Esse cursor
# funciona como o curso qunado estamos escrevendo

# OBS: A função read() lê todo o conteudo do arquivo
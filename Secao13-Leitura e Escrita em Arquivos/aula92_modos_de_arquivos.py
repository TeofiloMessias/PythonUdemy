"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo ja exista
x -> Abre para escrita somente se o arquivo não exisitir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o conteudo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e Escrita. ( Temos o controle do cursor)

# OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. caso exista, o novo conteúdo
será adicionado SEMPRE ao final do arquivo. Com o modo 'a' não controlamos o cursor.

http://doc.python.org/3/library/functions.html#open

# Exemplo X
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo 2. \n')
except FileExistsError:
    print('Arquivo já existe')


# Exemplo a
    with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
"""

# Exemplo r+
with open('outro.txt', 'r+') as arquivo:

    arquivo.write('No topo!\n')
    arquivo.seek(11)
    arquivo.write('Nova linha.\n')
    arquivo.seek(17)
    arquivo.write('Mais uma linha.\n')

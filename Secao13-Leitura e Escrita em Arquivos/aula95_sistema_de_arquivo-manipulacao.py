"""

Sistema de Arquivos - manipulação

# Descobrimos se um arquivo ou diretorio existe

import os

# Arquivo
print(os.path.exists('teo.txt')) # True
print(os.path.exists('frutas.txt')) # True

# Diretorio

# Path relativos
print(os.path.exists('teo.txt')) # True
print(os.path.exists('frutas.txt')) # True

# Path absolutos
print(os.path.exists('PythonUdemy\Secao01-Apresentacao\aula1_sobre_curso.py')) # True

# Criando arquivos

# Forma1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3

with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

import os

# criando arquivos

print(os.getcwd())

# os.mknod('arquivo-teste4.txt')
#
# os.mknod('C:\Users\re045002\PycharmProjects\university.txt')

# OBS: Se você estiver utilizando no MAC OS, pode haver um erro de PermissionError

# Criando um arquivo via mknode() se o arquivo já existir teremos o erro FileExistsError

# Criando diretórios - unicos ( um a um )
# Path Relativo
os.mkdir('templetes')

# Path Absoluto
os.mkdir('C:\Users\re045002\PycharmProjects\templetes')

# OBS:  Afunção mkdir() cria um diretorio se este não existir. Caso exista, teremos FileExistsError

import os
os.mkdir('C:\Users\re045002\PycharmProjects\etc\templetes')

# OBS: Se não tivemos permissão para criar o diretorio teremos um PermissionError

os.mkdir('templetes')

os.mkdir('templetes\geek')

os.mkdir('templetes\geek\university')

# Criando multi-diretórios ( árvore de diretórios )
os.makedirs('templetes\\geek\\university')

# OBS: Se já existir, teremos um FileexistsError

os.makedirs('templetes2\geek2\university2', exist_ok=True)

# Diretorios

os.rename('templetes2', 'geek2')

# OBS: Se o diretorio não existir teremos um FileNotFoundError

# OBS: Se o diretorio que queremos nomear não estiver vazio , termos um OSError

# Renomear arquivos e diretórios

# Arquvivos

os.rename('geek2\novo2\outro\text.txt', 'geek2\novo2\outro\geek.txt')

# ATENÇÃO! Tome cuidado com os comando de deleção. Ao deletar um arquivo ou diretorio, eles
# não vão para lixeira, eles somem.

os.remove('geek.txt')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# Se você informar um diretório ao invés de um arquivo, teremos um IsADrectoryError

# Remover diretórios vazios

os.rmdir('templestes')

# OBS: se o diretorio tiver qualquer conteúdo teremos um OSError

# OBS: Se o diretorio não existir teremos um FileNotFoundError

# Removendo uma árvore de arquivos
for arquivo in os.scandir('geek2'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove((arquivo.path))

# Podemos remover uma arvore de diretorios fazios

os.removedirs('geek2')

# Se algum dos diretorios contiver arquivos ou outros diretorios, o processo para

# ATENÇÃO !: Ao remover arquivos com python eles não vão para a lixeira. Eles vão embora!

# Importando a biblioteca send2trash ( Envia arquivos e diretórios para a lixeira )

# pip install send2trash -> caso de erro fazer a intalação do -> sudo apt-get install lsb-core

from send2trash import send2trash

os.remove('cesta1.txt') # Não vai para lixeira. É deletado imediatamente.

send2trash('cesta2.txt') # Vai para lixeira. Pode ser restaurado.
# Se o arquivo não existir teremos OSError

send2trash('teste') # Apagando um diretório

# Trabalhando com arquivos e diretórios temporarios
import os
import tempfile

# criando um diretorio temporario.
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final usamos um input so para mantermos
# os arquivos temporarios  'vivos' dentro dos blocos with.

# OBS: possivelmente, o código acima não irá funcionar se você estiver utilizando
# o Windows. Por conta deesse sistema trabalhar de forma diferente com arquivos
# temporarios.


# Criando um arquivo temporario

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek university\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporario só conseguimos escrever bits. Por isso, utilizamos 'b'

# Sem o bloco with

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
"""

import os
import tempfile

# https://docs.python.org/3library/os.html?high=osmodule-os

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek university\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()

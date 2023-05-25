"""
Sistema de Arquivos e Navegação

Para fazer uso de maipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os -> operating System - Sistema Operacional

# Fazer import
import os

# getcwd() -> pega current work diretory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd()) # PycharmProjects\pythonUdemy\PythonUdemy\Secao13-Leitura e Escrita em Arquivos

# Para mudar o diretório, podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd()) #PycharmProjects\pythonUdemy\PythonUdemy

os.chdir('..')
print(os.getcwd()) #PycharmProjects\pythonUdemy

# Podemos checar se um diretório é absoluto ou relativo
print(os.path.isabs('C:/Users/re045002/PycharmProjects/pythonUdemy/PythonUdemy')) # True
ou
#OBS: para usuários windows
# Se você, infelizmente, estiver utilizando um computador com Windows
# terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('C:\\Users\\re045002\\PycharmProjects\\pythonUdemy\\PythonUdemy'))

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # posix (linux e MAC), nt (Windows)

# Fazer import

import sys
print(sys.platform)

# '/home/geek/workspace/sistema'

print(os.getcwd())  # C:\Users\re045002\PycharmProjects

res = os.path.join((os.getcwd(), 'geek', 'university'))

os.chdir(res)

print(os.getcwd())

# veja que o os.path.join() recebe dois paramentros, sendo o primeiro o diretorio atual e o segundo
# diretorio wue sera juntado ao atual

# Podemos listar os arquivos e diretorios com o listdir()
print(len(os.listdir('C:\\')))
"""

import os

# Podemos listar os arquivos e diretorios com mais detalhes com scandir()

arquivos = print(list(os.scandir()))

scanner = os.scandir()
arquivos = list(scanner)
#print(arquivos)

print(arquivos[0].inode()) #
print(arquivos[0].is_dir()) # É um diretorio ? False
print(arquivos[0].is_file()) # É um arquivo ? False
print(arquivos[0].is_symlink()) # É um link simbólico ? False
print(arquivos[0].name) # Nome do Arquivo
print(arquivos[0].path) # Caminho do arquivo
print(arquivos[0].stat()) # Estatisticas

# Quando utilizamo sa função scandir() nos precisamos fecha-la, assim queando abrimos um arquivo

scanner.close()

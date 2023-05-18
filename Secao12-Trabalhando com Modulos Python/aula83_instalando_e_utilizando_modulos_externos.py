"""
Módulos Externos

Utilizamos o gerenciador de pacotes chamdos Pip - Python Installer Package

Voce pode conhecer todos os pacotes externos oficiais em:  https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal

# Instalando um modulo:

pip install nome-do-arquivo

# Instalando o pacote colorama

pip install colorama

# utilizando o pacote instalado

from colorama import init, Fore
init()
from colorama import Fore,Back,Style

print(Fore.RED + 'Geek University')
print(Fore.YELLOW + 'Geek University')
print(Fore.BLUE + 'Geek University')
print(Fore.MAGENTA + 'Geek University')
"""
import pydf

#pdf = pydf.generate_pdf('<h1> Geek University</h1><br/><br/><strong>Programa&ccedil;&atilde;o em Python: Essencial</strong>')
pdf = pydf.generate_pdf('<h1> Geek </h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

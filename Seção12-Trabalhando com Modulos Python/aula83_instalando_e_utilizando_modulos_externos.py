"""
Módulos Externos

Utilizamos o gerenciador de pacotes chamdos Pip - Python Installer Package

Voce pode conhecer todos os pacotes externos oficiais em:  https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal
"""

from colorama import init, Fore
init()
from colorama import Fore,Back,Style
print(Fore.RED + 'Geek University')
print(Fore.YELLOW + 'Geek University')
print(Fore.BLUE + 'Geek University')
print(Fore.MAGENTA + 'Geek University')
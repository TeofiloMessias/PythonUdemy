"""
nomes: list = ['Geek', 'University']

versoes: tuple = (3, 4, 5)

opcoes: dict = {'ar': True, 'banco_couro': True}

valores: set = {3, 4, 5, 6}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)

https:www.alt-codes.net/suit-cards.php
"""

from typing import Dict, List,Tuple, Set
nomes: List[str] = ['Geek', 'University']

versoes: Tuple[int,int,int] = (3, 4, 5)

opcoes: Dict[str, bool] = {'ar': True, 'banco_couro': True}

valores: Set[int] = {3, 4, 5, 6}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)


"""
Ambiente Virtual Python
Na aula de preparação do ambiente fizemos a instalação de duas bibliotecas interessantes: - virtualenv
- virtualenvwrapper
Estas ferramentas são muito poderosas e nos permite criar ambientes isolados de
desenvolvimento Python, ou seja, torna possível a utilização de diversas bibliotecas em um
mesmo ambiente sem que haja conflitos.

Ambiente Virtual Python
Quando desenvolvemos com Python “globalmente”, ou seja, diretamente com o Python
instalado no sistema operacional, ao invés de isomarlos os ambientes de cada projeto em
desenvolvimento, podemos ter conflitos entre versões de bibliotecas. Podemos por exemplo desenvolver um projeto onde determinada biblioteca, por exemplo
‘colorama’ só seja possível usar com Python 3.4 e em outro projeto fazermos uso de uma
biblioteca, por exemplo ‘numpy’ na qual queremos usar os últimos recursos do Python 3.8.5. Se não tivermos ambientes virtuais com o isolamento não seria possível fazer isso

Ambiente Virtual Python
O funcionamento do virtualenv é bastante simples, ele
basicamente cria uma cópia de todos os diretórios
necessários para que um programa Python seja executado. Desta forma, ao instalar uma nova biblioteca dentro do
ambiente virtual criado, esta biblioteca será colocada no
diretório do virtualenv e não mais de forma global no
sistema operacional.

Ambiente Virtual Python
Desta forma, um programador profissional Python irá criar
para cada projeto um ambiente virtual, de preferência com
o mesmo nome do projeto para que seja fácil encontrar e
fazer uso. Por exemplo, imaginando que temos um projeto de um e- commerce, podemos criar um ambiente virtual conforme:
mkvirtualenv ecommerce
Ao usar o PyCharm ou outra IDE, devemos criar um projeto
com este mesmo nome. OBS: No PyCharm ao criar um novo projeto Python será
criado um ambiente virtual automaticamente com o mesmo
nome do projeto criado
"""
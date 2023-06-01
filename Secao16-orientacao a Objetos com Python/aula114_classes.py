"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados
computacionalmente.

Imagine que voce queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
     - Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos conseguimos
    representar computacionalamente os estados de um objeto. No caso da lâmpada, possivelmente
    iriamos querer saber se a lãmpada é 10 ou 220 volts, se ela é branca, amarela,vermelha ou
    outra cor, qual é a luminosidade dela e etc.

    - Métodos (funções) -> Representam os comportamentos do objeto, Ou seja , as ações que este
    objeto pode realizar no seu sistema. Nocaso da lãmpada, por exemplo, um comportamento comum
    que muito provavelmente iríamos querer representar no nosso sistema é o de ligar e desligar
    a mesma.


Em Python para definir uma Classe utilizaos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python qunado temos um bloco de código que ainda esta
implementado.

OBS: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial
em maiúsculla. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em
maiúscilas, todas juntas

Dica : Em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares
para nomes de class, atributos,métodos,arquivos, diretórios e etc.

OBS> Quando estamos pranejando um software e definimos quais classesteremos que ter no sistema, chamamos
estes objetos que serão mapeados para classes de entidades.
"""

class Lampada:
    pass

class ContaCorrente:
    pass

class Produto:
    pass

class usuario:
    pass



lamp = Lampada()

print(lamp)
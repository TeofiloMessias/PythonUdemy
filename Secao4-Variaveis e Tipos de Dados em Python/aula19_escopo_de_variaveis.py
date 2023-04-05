"""
Escopo de variáveis

Dois casos de escopo

1 - variáveis globais;
    - Variaveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variaveis locais;
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas ou seja seu escopo
    esta limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que
ao declaramos uma variavél, nos não colocamos o tipo de dado dela.
Este tipo é inferido ao atributo o valor da mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42
"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

# Reatribuição de valor
numero = 'Geek'
print(numero)
print(type(numero))

numero = 42
novo = 0

if numero > 42:
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do bloco do if.Portanto é local
    print(novo)

print(novo)

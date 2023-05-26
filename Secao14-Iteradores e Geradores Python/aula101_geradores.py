"""
Geradores

- Geradores (Generators) são Iteratos (Iteradores);

OBS: O contrario não é verdadeiro. Ou seja, nem todo iterator é um generator.

outras informações:
- Genarators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com a Expressão Geradoras;

Diferenças entre Funções e Generator Functions ( Funções Geradoras )

----------------------------------------------------------------------------------
| Funções                                | Generatos Functions                   |
----------------------------------------------------------------------------------
| utilizam return                        | utilizam yield                        |
----------------------------------------------------------------------------------
| rena uma vez                           | podem utilizar yield multiplas vezes  |
----------------------------------------------------------------------------------
| qunado executada, retorna um valor     | quando executada, retorna um generator|
----------------------------------------------------------------------------------

for num in gen:
    print(num)

gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for num in gen:
    print(num)
"""

# Exemplo Função Geradora ( Generator Function )

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Um Generator Function não é um Generator. ela gera um generator. OK ?

gen = list(conta_ate(10))

print(gen)

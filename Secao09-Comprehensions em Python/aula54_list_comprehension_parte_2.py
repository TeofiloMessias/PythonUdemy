"""
List Comprehension - Parte 2

Nós podemos adicionar estruturas condicionais lógicas as nossas List Comprehension
"""

# Exemplo

# 1

numeros = [1,2,3,4,5,6]

pares = [numeros for numero in numeros if numeros % 2 ==0]
impares = [numeros for numeros in numeros if numeros % 2 !=0]

print(pares)
print(impares)

# Refatorar

# Qualquer numero par modulo de 2 é 0 e 0 em Python é FALSE. not False = True
pares = [numero for numero in numero if not numero % 2]

# Qualquer numero impar moulo de 2 é 1, e 1 em Python é TRUE
impares = [numero for numero in numero if numero % 2]

print(pares)
print(impares)

# 2

res =[numero * 2 if numero % 2 == 0 else numero /2 for numero in numeros]
print(res)
"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort\0 que já estudamos em Listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer interável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted SEMPRE retorna uma lista com os elemetnos do interável ordenados.

# Exemplo

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros)) # Ordenar do menor para o maior

print(numeros) # A lista principal não muda.

numeros =[6,1,8,2]
print(numeros)

print(sorted(numeros))

# Adiciona parãmetros ao sorted()

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

# Podemos utulizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro boloes", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": [" Eu amo meu gato "]},
    {"username": "jeff", "tweets": [" "]},
    {"username": "bob123", "tweets": [" "]},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [" "]}
]

print(usuarios)

# Ordenada por username - Orddem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenada pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

"""

# Ultimo exemplo

musicas = [
    {"titulo": "Thunderstruck ", "tocou": 3},
    {"titulo": " Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black ", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die ", "tocou": 32}
]

# Ordena da menos tocada para a mais tocada.
print(sorted(musicas, key=lambda musica: musica["tocou"]))

# Ordena da mais tocada para a menos tocada.
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))

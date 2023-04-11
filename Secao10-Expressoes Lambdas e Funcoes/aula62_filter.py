"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

valores = 1, 2, 3, 4, 5, 6
media = (sum(valores) / len(valores))
print(media)

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

# OBS: Assim como a função map(), a filter() recebe dois parãmetros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(list(res))
# OBS: Assim como na função map(), apos serem utilizados os dados de filter() eles são excluidos da memória.

paises = [' ', 'Agentina', ' ', 'Brasil', 'Chile', ' ', 'Colombia', ' ', 'Equador', ' ', ' ', 'Venezuela']

print(paises)

res = filter(None, paises) # O None remove os espaços vazios
#res = filter(lambda pais: len(paises) > 0, paises)
#res =filter(lambda pais: paises != '', paises) # Outra forma de filtrar os campos vazios
print(list(res))

# A diferença entre map() e filter é:
# Map retorna valores que não seja true e false.

# map() -> Recebe dois parâmentros, e uma função e um interável e retorna um objeto mapeando a função para cada elemento do iteravel.

# filter() -> Recebe dois parametros, uma função e um iteravel e retorna um objeto filtrando apenas os elementos de acordo com a função.
# filter() retorna sempre 'TRUE' ou 'FALSE'.

# Exemplo mais complexo.

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro boloes", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": [" Eu amo meu gato "]},
    {"username": "jeff", "tweets": [" "]},
    {"username": "bob123", "tweets": [" "]},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [" "]}
]
print(usuarios)

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets'] == 0, usuarios)))
print(inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets', usuarios]))
print(inativos)
"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Marcia']

# Devemos criar uma lista contendo 'Sua istrutora é' + nome, desde que cada nome tenha nemos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)


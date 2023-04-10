"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.
"""

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
import math

# math.prod - retorna o produto de um container numérico

nuns_v1 = [2, 3, 6, 8]
nuns_v2 = (2, 3, 6, 8)
nuns_v3 = {2, 3, 6, 8}

# print(math.prod(nuns_v1))
# print(math.prod(nuns_v2))
# print(math.prod(nuns_v3))

"""
2 * 3 * 6 * 8
"""

# math.isqrt - retorna a parte inteira da raiz quadrada de um número

# print(math.isqrt(9))
# print(math.qrt(9))
# print(math.isqrt(17))
# print(math.qrt(17))

# math.dist - retorna a distancia euclidiana entre dois pontos, 3D ou 2D

# Pontos 3D

ponto3D_d1 = (12, 50, 40)
ponto3D_d2 = (6, 7, 13)

# Pontos 2D
ponto2D_d1 = (12, 50)
ponto2D_d2 = (6, 7)

# print(math.dist(ponto3D_d1, ponto3D_d2))
# print(math.dist(ponto2D_d1,ponto2D_d2))

# math.hypot - retorna a hipotenusa, ou norma Euclidiana

# print(math.hypot(*ponto3D_d1))
# print(math.hypot(*ponto2D_d1))

# Estatística
import statistics

# statistics.fmean - calcula a média de números reais

valores_reais = [1.45, 6.789, 89.98765]
valores_inteiros = [1, 6, 3, 89]

# print(statistics.fmean(valores_reais))
# print(statistics.fmean(valores_inteiros))

# statistics.geometric_mean - calcula geométrica de numeros reais
# print(statistics.geometric_mean(valores_reais))
# print(statistics.geometric_mean(valores_inteiros))

seq1 = 'Geek University'
seq2 = [3, 5, 3, 8, 7, 8, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
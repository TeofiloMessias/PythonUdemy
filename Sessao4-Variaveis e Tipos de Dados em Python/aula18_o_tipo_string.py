"""
O Tipo String

Em Python, um dado é considerado do tipo string sempre que:

-Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
-Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
-Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome2 = "Gina's Bar"
print(nome2)
print(type(nome2))

nome3 = 'Angelina \nJolie'
print(nome3)
print(type(nome3))

nome3 = "Angelina Jolie"
print(nome3)
print(type(nome3))

nome4 = 'Angelina \" Jolie'
print(nome4)
print(type(nome4))

print(nome.upper())

print(nome.lower())

print(nome.split())# Transforma em uma lista de strings

print(nome[0:4])  # Slice de string

print(nome[5:15])  # Slice de string

#[ 0,       1]
#['Geek', 'University']

print(nome.split()[0])

print(nome.split()[1])


"""
# Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

#[ 0,  1 , 2,  3,  4,   5,  6,  7,  8,  9,  10, 11, 12, 13,14 ]
#['G','e','e','k',' ', 'U','n','i','v','e','r','s','i','t','y']
nome = 'Geek University'
"""
[::-1] -> Comece do primeiro elemento, vá até o ultimo elemento e inverta
"""
print(nome[::-1]) #Inversão da String  Pythônico
print(nome.replace('G','P'))
print(type(nome))

texto = 'socorram me subino onibus em marrocos' #Palíndromo
print(texto)

print(texto[::-1])


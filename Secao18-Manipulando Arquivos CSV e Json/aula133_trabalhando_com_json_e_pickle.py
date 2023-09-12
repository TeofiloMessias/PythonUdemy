"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicalção entre os serviços oferecidos por empressas
(Twitter, Facebook, Youtube..) e terceiros (nós desenvolvedores).

import json

ret = json.dumps(['produto',{'Playstation4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))

print(ret)

import json

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Feliz', 'Bira-Lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)

Integrando o JSON com Pickle

pip install jsonpickle

import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Feliz', 'Bira-Lata')

ret = jsonpickle.econde(felix)

print(ret)

# Escrevendo o arquivo json/pickle

import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Feliz', 'Bira-Lata')

with open('felix.json','w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)


"""
# Lendo o arquivo json/pickle

import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Feliz', 'Bira-Lata')

with open('felix.json','r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)


"""
Seek e Cursosrs

seek() -> É utilizado para movimentar o cursos pelo arquivo

arquivo = open('texto.txt')

print(arquivo.read())

# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um
# parâmetro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek() -> Procurar

arquivo.seek(22)

print(arquivo.read())

# readline() -> Função que lê o arquivo linha a linha ( readline -> lê linha)

ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' '))

# readlines()

linhas = arquivo.readlines()

print(len(linhas))

#OBS: Qunado abrimos um arquivo om a função open() é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivo devemos fechar essas conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;

"""
#1 - Abrir o arquivo;
arquivo = open('texto.txt')

#2 - Trabalhar o arquivo;
print(arquivo.read())

#3 - Fechar o arquivo;
arquivo.close()




"""
POO - Métodos Mágicos

Metodos magicos, são todos os métos que utilizam dunder

# dunder init - > __init__()
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

Dunder > Double Underscore

dunder repr -> Representação do objeto
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

# O método str é prioridade
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um Objeto do tipo Livro foi deletado da memoria')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msn = ''
            for n in range(outro):
                msn += ' ' + str(self)
            return msn
        return 'Não posso multiplicar'

livro1 = Livro('Python Rocks!','Geek University', 400)
livro2 = Livro('Inteligencia Artificial em Python !','Geek University', 350)

print(livro1)
print(livro2)

print(len(livro1))

print(livro1 + livro2)

print(livro1 * 7)

print(livro1 * 'Geek')

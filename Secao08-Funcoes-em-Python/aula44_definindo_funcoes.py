"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas especificas;
- Pode ou não receber entradas de dados e retornar um saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que inicamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;
"""
# Exemplos de utilização de funções:

# cores =['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada(Built-in) do Python print()

# print(cores)

# curso = 'Programação em Python: Essencial'

# print(curso)

# cores.append('roxo')

# print(cores)

# curso.append('mais dados...') # AttributeError
# print(curso)

# cores.clear()
# print(cores)

# print(help(print))
# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código

# Mas então, como definir funções ?
"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por underline(Snake Case)
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processo da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Vej aque para definr uma função, utilizamos a palavra reservada 'def' informando ao Python que
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é
utilizados em Python para definr blocos.
"""

# Definindo a primeria função

# Definição
def diz_oi():
    print('Oi')

"""
OBS:

1 - Veja que, dentro das nossa função podemos utilizar outra função;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmentro de entrada;
4 - Veja que esta função não retorna nada
"""
# Utilizando funções

# Chamada de execução
diz_oi()

"""
ATENÇÃO:

nunca esqueça de utlizar o parenteses ao executar uma função

Exemplo:

# Errado!
diz_oi

# Certo
diz_oi()

# Errado
diz_oi ()
"""

# Exemplo 2

def cantar_parabens():
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

cantar_parabens()

#for n in range(5) # vai executar 4
#    print(n)
#    cantar_parabens()

# Em Python, podemos inclusive criar variaveis do tipo de uma função e executar esta função através da variável

canta = cantar_parabens

canta()
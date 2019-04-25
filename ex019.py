# 019 - Sorteie um dos quatro alunos para apagar o quadro.

from random import choice, shuffle, random

al1 = str(input('Digite o nome do aluno 1: '))
al2 = str(input('Digite o nome do aluno 2: '))
al3 = str(input('Digite o nome do aluno 3: '))
al4 = str(input('Digite o nome do aluno 4: '))

lista_alunos=[al1, al2, al3, al4]
alunos = choice(lista_alunos)

print('O Aluno escolhido para apagar o quadro foi: {}'.format(alunos))
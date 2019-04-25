# 020 - Sortear a ordem de apresentação de quatro alunos.

from random import shuffle


al1 = str(input('Digite o nome do aluno 1: '))
al2 = str(input('Digite o nome do aluno 2: '))
al3 = str(input('Digite o nome do aluno 3: '))
al4 = str(input('Digite o nome do aluno 4: '))

lista_alunos=[al1, al2, al3, al4]

shuffle(lista_alunos)

print('A ordem de apresentação dos alunos será a seguinte: {}'.format(lista_alunos))

contal = 0
for aluno in lista_alunos:
    print('O aluno {} será: {}'.format(contal, aluno))
    contal += 1
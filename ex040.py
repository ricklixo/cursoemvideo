# Desafio 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# -Média abaixo de 5.0: Reprovado
# -Média entre 5.50 e 6.9: Recuperação
# -Média 7.0 ou superior: Aprovado

nota1 = float(input('Digite a Nota 1: '))
nota2 = float(input('Digite a Nota 2: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua média ficou em {}. REPROVADO'.format(media))
elif media >= 5.0 and media < 6.9:
    print('Sua média ficou em {}. RECUPERAÇÃO'.format(media))
else:
    print('Sua média ficou em {}. APROVADO.'.format(media))
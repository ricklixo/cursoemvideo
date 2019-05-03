# 028 - Algoritmo de número entre 0 e 5, o usuário precisa adivinhar e o computador informar se ele  venceu ou perdeu.

# MINHA SOLUÇÃO
from random import randint
escolha = 'S'
while escolha == 'S':
    num_cpu = randint(0, 5)
    num = int(input('Escolha um número entre 0 e 5: '))
    if num <= 5:
        print('Numero escolhido: {}'.format(num))
        print('Numero CPU: {}'.format(num_cpu))
        if num == num_cpu:
            print('Parabéns, você venceu!!!')
        else:
            print('Não foi dessa vez...')
    else:
        print('Escolha um número entre 0 e 5. ')
    escolha = str(input('Deseja tentar novamente? [S/N]? ')).strip().upper()


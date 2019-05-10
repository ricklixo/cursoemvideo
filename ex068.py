# 068 - Faça um programa que jogue PAR ou IMPAR com o computador.
# O jogo será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no jogo.

# MINHA SOLUÇÃO
from random import choice
from random import randint

vitoria = 0
while True:
    sorteio = randint(0, 11)
    print('''    [1] IMPAR
    [2] PAR''')
    jogador = int(input('Escolha sua opção: '))
    if jogador == 1:
        if sorteio % 2 !=0:
            print(f'Você escolheu IMPAR e o cpu escolheu PAR. O resultado foi {sorteio}. Você venceu!')
            vitoria += 1
        else:
            print(f'Você escolheu IMPAR e o cpu escolheu PAR. O resultado foi {sorteio}. Você perdeu :(')
            break
        print(sorteio)
    elif jogador == 2:
        if sorteio % 2 == 0:
            print(f'Você escolheu PAR e o cpu escolheu ÍMPAR. O resultado foi {sorteio}. Você venceu!')
            vitoria += 1
        else:
            print(f'Você escolheu PAR e o cpu escolheu ÍMPAR. O resultado foi {sorteio}. Você perdeu :(')
            break
print(f'Total de vitórias consecutivas: {vitoria}')


# SOLUÇÃO GUANABARA
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PpIi':
        tipo = str(input('PAR ou ÍMPAR')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {vitoria} vezes')

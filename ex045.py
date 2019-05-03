# DESAFIO 045 - Crie um programa que faça o computador jogar JOKENPÔ com você.

from random import choice
jankenpo = ['PEDRA', 'PAPEL', 'TESOURA']

cpu = choice(jankenpo)
selecao = ' '
print('[1] - PEDRA')
print('[2] - PAPEL')
print('[3] - TESOURA')
escolha_jogador = int(input('Escolha sua opção: '))

if escolha_jogador == 1:
    selecao = 'PEDRA'
if escolha_jogador == 2:
    selecao = 'PAPEL'
if escolha_jogador == 3:
    selecao = 'TESOURA'

if (selecao == 'PEDRA' and cpu == 'PEDRA') or (selecao == 'PAPEL' and cpu == 'PAPEL') or ( selecao == 'TESOURA' and cpu == 'TESOURA'):
    print('ESCOLHA CPU: {}'.format(cpu))
    print('ESCOLHA JOGADOR: {}.'.format(selecao))
    print('EMPATE')
elif (selecao == 'PEDRA' and cpu == 'TESOURA') or (selecao == 'PAPEL' and cpu == 'PEDRA') or ( selecao == 'TESOURA' and cpu == 'PAPEL'):
    print('ESCOLHA CPU: {}'.format(cpu))
    print('ESCOLHA JOGADOR: {}.'.format(selecao))
    print('VITÓRIA')
elif (selecao == 'PEDRA' and cpu == 'PAPEL') or (selecao == 'PAPEL' and cpu == 'TESOURA') or ( selecao == 'TESOURA' and cpu == 'PEDRA'):
    print('ESCOLHA CPU: {}'.format(cpu))
    print('ESCOLHA JOGADOR: {}.'.format(selecao))
    print('DERROTA')

# 058 - Melhore o jogo do DESAFIO 028, onde o computador vai pensar em um número de 0 a 10. Agora o jogador vai tentar adivinhar até acertar, mostrando
# no final quantos palpites foram necessários

# MINHA SOLUÇÃO
from random import randint

palpites = 0
cpu = randint(0, 10)

while True:
    jogador = int(input('Digite um número entre 0 e 10: '))
    palpites += 1
    if jogador == cpu:
        break
print('Você venceu depois de {} tentativas'.format(palpites))

# SOLUÇÃO GUANABARA
print('Sou seu comptuador.. acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False # enquanto eu utilizei BREAK, o guanabara utilizou booleanos.
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == cpu:
        acertou = True
    else:
        if jogador < cpu:
            print('Mais.. tente mais uma vez.')
        elif jogador > cpu:
            print('Menos.. tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns'.format(palpites))



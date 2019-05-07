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


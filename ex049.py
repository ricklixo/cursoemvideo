# Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando o laço for

# MINHA SOLUÇÃO
num = int(input('Digite um número de 1 a 10: '))
print('TABUADA DE {}'.format(num))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(num, c, (num * c)))
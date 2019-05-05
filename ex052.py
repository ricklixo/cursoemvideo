# 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

# SOLUÇÃO GUANABARA - não consegui.
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
print('{} foi divisível {} vezes.'.format(c, tot), end='')
if tot == 2:
    print(' Logo, É um número primo')
else:
    print(' Por isso, NÃO É um número primo.')

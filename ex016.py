# 016 - Leia um número real qualquer e mostre na tela sua porção inteira.

from math import trunc

num = float(input('Digite um número qualquer: '))

print('O número real {} convertido para inteiro é igual a {}'.format(num, trunc(num)))



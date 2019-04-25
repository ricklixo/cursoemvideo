# 017 - Leia o comprimento do cateto oposto e adjacente de um triangulo, calcule o comprimento da hipotenusa.

from math import hypot

cato = float(input('Digite o valor do cateto oposto: '))
cata = float(input('Digite o valor do catato adjacente: '))

print('O comprimento da hipotenusa é igual a {}'.format(hypot(cato, cata)))


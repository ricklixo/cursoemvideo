import math
import os

arquivo = open('files/listamath.txt', 'w')

matematica = dir(math)
lista = []
for mat in matematica:
   lista.append(mat)

for palavra in lista:
    arquivo.write(palavra + '\n')

arquivo.close()

arquivo = open('files/listamath.txt', 'r')
f = arquivo.read()

print(f)
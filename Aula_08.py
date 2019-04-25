# UTILIZANDO MÓDULOS

import math # importa todas as funcionalidades

num = int(input('Digite um número: '))

raiz = math.sqrt(num)

print('A Raiz de {} é igual a {:.2f}'.format(num, raiz))

import random
num1 = random.randint(1, 10)
print(num1)
print(dir(random))
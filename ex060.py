# 060 - Faça um programa que leia um número qualquer e mostre seu fatorial.

# MINHA SOLUÇÃO
num = int(input('Digite um número inteiro: '))
r = num
while num > 1:
    print('{} x'.format(num), end=' ')
    num -= 1
    if num == 1:
        print('1 = ')
    r = num * r
print('{}'.format(r))

# SOLUÇÃO GUANABARA - BEM MAIS ELEGANTE
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print('{}'.format(f))

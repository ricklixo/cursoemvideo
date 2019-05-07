# 060 - Faça um programa qe leia um número qualquer e mostre seu fatorial.

# MINHA SOLUÇÃO
num = int(input('Digite um número inteiro: '))
cont = 1
r = num
while num > 1:  
    print('{} x'.format(num), end=' ')
    num -= 1
    if num == 1:
        print('1 =')
    r = num * r
print(r, end = ' ')
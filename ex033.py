# 033 - faça um programa que leia 3 numeros e mostre qual é o maior e o menor

n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
n3 = int(input('Digite o número 3: '))

print('O maior número entre {}, {} e {} é: {}'.format(n1, n2, n3, max(n1, n2, n3)))
print('O menor número entre {}, {} e {} é: {}'.format(n1, n2, n3, min(n1, n2, n3)))

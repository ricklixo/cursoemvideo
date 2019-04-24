# Desafio 06 - Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))

dobro = num * 2
triplo = num * 3
raiz = num**(1/2)


print('O número digitado foi: {}. \nSeu dobro é {}. \nSeu triplo é {}. \nSua raiz quadrada é {:.3f}.'.format(num, dobro, triplo, raiz))
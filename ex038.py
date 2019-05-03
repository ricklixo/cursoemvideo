# Desafio 038 - Escreva um programa que leia dois numeros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, ambos são iguais.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('N1: {}, N2: {} - Maior: {}'.format(n1, n2, n1))
elif n2 > n1:
    print('N1: {}, N2: {} - Maior: {}'.format(n1, n2, n2))
else:
    print('Ambos os números são iguais.')

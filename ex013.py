# Desafio 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário? R$: '))

aumento = salario + (salario * 15/100)

print('O salário atual do funcionário é de R$ {:.2f}. \nDevido a uma promoção, teve um aumento de 15%, passando a ganhar R$ {:.2f}.'.format(salario, aumento))

# Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

palavra = input('Digite algo no prompt: ')

print('O tipo primitivo é {}'.format(type(palavra)))
print('Caixa alta? {}'.format(palavra.isupper()))
print('Caixa baixa? {}'.format(palavra.islower()))
print('Modo título? {}'.format(palavra.istitle()))
print('É numérica? {}'.format(palavra.isnumeric()))
print('É alfa numérica? {}'.format(palavra.isalnum()))
print('É alfabética? {}'.format(palavra.isalpha()))
print('É decimal? {}'.format(palavra.isdecimal()))
print('Possui espaços? {}'.format(palavra.isspace()))
print('Pode ser impressa? {}'.format(palavra.isprintable()))








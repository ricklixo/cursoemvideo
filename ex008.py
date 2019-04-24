# Desafio 08 - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metros = float(input('Digite a medida que deseja em Metros: '))

cm = metros * 100
mm = metros * 1000

print('{} Metros convertidos para Centimetros é igual a {} cm.'.format(metros, cm))
print('{} Metros convertidos para Milímetros são iguais a {} mm'.format(metros, mm))
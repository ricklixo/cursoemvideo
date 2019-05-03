# Desafio 043 - Crie um programa que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = int(input('Digite seu peso (KG): '))
altura = float(input('Digite sua altura (Metros): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('IMC: {:.2f} - Abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC: {:.2f} - Peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC: {:.2f} - Sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC: {:.2f} - Obesidade'.format(imc))
else:
    print('IMC: {:.2f} - Obesidade mórbida'.format(imc))

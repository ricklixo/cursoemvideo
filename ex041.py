# Desafio 041 - Crie um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# -Até 9 anos: Mirim
# -Até 14 anos: Infantil
# -Até 19 anos: Junior
# -Até 25 anos: Senior
# -Acima : Master

from datetime import date

ano_atual = date.today().year
nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = ano_atual - nasc

if idade >=3 and idade <=9:
    print('Categoria: MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')
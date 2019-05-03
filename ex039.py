# Desafio 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - se é a hora de se alistar
# - se já passou do tempo de alistamento
# O programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year

data_nascimento = int(input('Informe o ano de seu nascimento: '))
idade = ano_atual - data_nascimento

if idade < 18:
    print('Você tem {} anos, ainda não é hora de se alistar! Yay!'.format(idade))
    print('Ainda faltam {} anos.'.format(18 - idade))
elif idade == 18:
    print('Você tem {} anos, infelizmente é hora de se alistar....'.format(idade))
else:
    print('Você tem {} anos, se não se alistou, deverá comparecer à junta militar.'.format(idade))
    print('Tempo já passado do prazo: {} anos.'.format(idade - 18))
    print('Seu alistamento foi em: {}'.format(ano_atual - (idade - 18)))


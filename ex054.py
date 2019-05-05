#054 -  Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas 
# ainda não atingiram a maioridade e quantas já são maiores

# MINHA SOLUÇÃO
from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano_nascimento = int(input('Digite o {}º ano de nascimento: '.format(c)))
    if (ano_atual - ano_nascimento) >= 21:
        maior += 1
    else:
        menor += 1
print('Maiores de idade: {} pessoas'.format(maior))
print('Menores de idade: {} pessoas'.format(menor))

# SOLUÇÃO GUANABARA - basicamente igual a minha.

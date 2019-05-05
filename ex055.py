# 055 - Faça um programa que leia o peso de cinco pessoas e no final mostre qual o maior e o menor peso lidos


# MINHA SOLUÇÃO
maior_peso = 0
menor_peso = 1000 # NÃO é o ideal.

for c in range(1, 6):
    peso = int(input('Digite o peso {}: '.format(c)))
    if peso >= maior_peso:
        maior_peso = peso
    if peso <= menor_peso:
        menor_peso = peso
print('Maior peso: {}'.format(maior_peso))
print('Menor peso: {}'.format(menor_peso))

# SOLUÇÃO GUANABARA
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso {}: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))

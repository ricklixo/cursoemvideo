# 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa pergunta
# se o usuário quer continuar ou não. No final, mostre:
# a) quantas pessoas tem mais de 18 anos.
# b) quantos homens foram cadastrados.
# c) quantas mulheres tem menos de 20 anos.

# MINHA SOLUÇÃO
maior_dezoito = 0
homens = 0
mulheres_vinte = 0

while True:
    idade = int(input('Digite a idade da pessoa: '))

    sexo = ' ' # é necessário sempre colocar um espaço vazio. Se não houver um espaço, não funciona
    while sexo not in 'MF': # Essa instrução evita a inserção de comandos errados, como letras diferentes.
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior_dezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_vinte += 1
    continuar = ' '
    while continuar not in 'SN': # Essa instrução evita a inserção de comandos errados, como letras diferentes.
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Mais de dezoito anos: {maior_dezoito}')
print(f'Total de homens: {homens}')
print(f'Mulheres com menos de 20: {mulheres_vinte}')


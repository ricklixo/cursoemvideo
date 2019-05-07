# 057 -  Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um 
# valor correto

sexo = ''
while sexo in 'MF':
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if 'M' != sexo != 'F':
        print('Valor inválido, digite novamente.')
        sexo = 'F'
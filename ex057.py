# 057 -  Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um 
# valor correto

# MINHA SOLUÇÃO - Talvez refazer depois. Deixei em loop eterno, e não era ideal
sexo = ''
while sexo in 'MF':
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if 'M' != sexo != 'F':
        print('Valor inválido, digite novamente.')
        sexo = 'F'

# SOLUÇÃO GUANABARA
sexo = str(input('Inform seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF': # ele utiliza o laço para verificar a resposta negativa.
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

# 056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final mostre:
# a média de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos.


# MINHA SOLUÇÃO
mulheres_vinte = 0
anos_totais = 0
idade_homem = 0
homem_velho = ''

for c in range(1, 5):
    print('----- {}ª Pessoa -----'.format(c))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    anos_totais += idade
    if idade <= 20 and sexo == 'F':
        mulheres_vinte += 1
    if sexo == 'M':
        if idade >= idade_homem:
            idade_homem = idade
            homem_velho = nome

media_idade = anos_totais / 4
print('Média de idade do grupo: {} anos'.format(media_idade))
print('Mulheres com menos de 20: {}'.format(mulheres_vinte))
print('Nome do homem mais velho: {}'.format(homem_velho))
    
# SOLUÇÃO GUANABARA
for p in range(1, 5):
    print('---- {}ª Pessoa ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    anos_totais += idade
    if p == 1 and sexo in 'Mn':
        idade_homem = idade
        homem_velho = nome
    if sexo in 'Mn' and idade > idade_homem:
        idade_homem = idade
        homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres_vinte += 1
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velhor tem {} anos e se chama {}.'.format(idade_homem, homem_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres_vinte))
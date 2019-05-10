# 070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
# vai continuar. No final mostre:
# a) qual é o total gasto na compra.
# b) quantos produtos custam mais de R$ 1000.
# c) qual é o nome do produto mais barato.

# MINHA SOLUÇÃO
total_gasto = 0
produtos_mil = 0
produto_barato = ''
menor_valor = 0
cont = 0
while True:
    nome_produto = str(input('Digite o nome do produto: ')).upper()
    preco_produto = float(input('Digite o preço do produto (R$): '))
    total_gasto += preco_produto
    cont += 1
    if preco_produto > 1000:
        produtos_mil +=1
    if cont  == 1:
        menor_valor = preco_produto
        produto_barato = nome_produto
    else:
        if preco_produto < menor_valor:
            menor_valor = preco_produto
            produto_barato = nome_produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('DESEJA CONTINUAR [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total gasto na compra R$: {total_gasto:.2f}')
print(f'Produtos que custam mais de R$ 1000: {produtos_mil}')
print(f'Produto mais barato: {produto_barato}')



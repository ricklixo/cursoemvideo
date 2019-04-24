# Desafio 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.


produto = float(input('Digite o preço de um produto em reais (R$): '))

desconto = produto - (produto * 5/100)
print('Devido a uma queima de estoque, o produto que custava R$ {:.2f} teve um desconto de 5% e seu valor passou a ser R${:.2f}'.format(produto, desconto))


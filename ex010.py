# Desafio 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Dolar = R$ 3.27

dinheiro = float(input('Digite quantos Reais (R$ Você possui na carteira: '))

dolar = dinheiro / 3.27

print('Você possui R$ {:.2f} em sua carteira. \nCom essa quantia é possível comprar US$ {:.2f} .'.format(dinheiro, dolar))


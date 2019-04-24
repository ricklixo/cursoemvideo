# Desafio 05 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número inteiro: '))

ante = num - 1
suc = num + 1

print('O numero digitado foi {}. Seu antecessor é {} e seu sucessor é {}'.format(num, ante, suc))


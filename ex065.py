#065 - Crie um programa que leia vários números  inteiros. No final, mostre a media entre todos os valors e qual foi o maior e o menor. O programa deve
# perguntar se o usuário quer continuar a digitar valores

# MINHA SOLUÇÃO
continuar = 'S'
cont_media = 0
soma = 0
maior = 0
menor = 99999

while continuar == 'S':
    n = int(input('Digite um número inteiro: '))
    cont_media += 1
    soma += n
    if n >= maior:
        maior = n
    if n <= menor:
        menor = n
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()

media = soma / cont_media
print('Soma dos números: {}'.format(soma))
print('Media dos números: {:.2f}'.format(media))
print('Maior número digitado: {}'.format(maior))
print('Menor número digitado: {}'.format(menor))
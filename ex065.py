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
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
media = soma / cont_media
print('Soma dos números: {}'.format(soma))
print('Media dos números: {:.2f}'.format(media))
print('Maior número digitado: {}'.format(maior))
print('Menor número digitado: {}'.format(menor))


#SOLUÇÃO GUANABARA
resp = 'S'
quant = 0
maior_num = 0
menor_num = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior_num = menor_num = num
    else:
        if num > maior_num:
            maior_num = num
        if num < menor_num:
            menor_num = num
    resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
media = soma / quant
print('Acabou.')
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor {} e o menor foi {}'.format(maior_num, menor_num))

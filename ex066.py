# 066 - Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 999.
# No final mostre quantos numeros foram digitados e qual foi a soma entre eles (Desconsiderando o flag).

soma = quant = 0
while True:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        break
    soma += num
    quant +=1
print(f'A soma dos {quant} números digitados foi igual a {soma}')

# 064 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição
# de parada. No final mostra quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)

# MINHA SOLUÇÃO
soma = 0
total_num = 0
num = 0
while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        soma += num
        total_num += 1
print('Soma total dos números: {}'.format(soma))
print('Total de números somados: {}'.format(total_num))

# SOLUÇÃO GUANABARA
numero = cont = soma = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} valores e a soma total foi {}'.format(cont, soma))

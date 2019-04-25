#023 - faça um programa que leia um número de 0 a 9999 e mostre cada um dos digitos separados

# SOLUÇÃO GUANABARA: NÃO CONSEGUI FAZER

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))


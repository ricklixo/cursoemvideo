# 050 - Leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o

# MINHA SOLUÇÃO
n = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o número {}:'.format(c)))
    if num % 2 == 0:
        n += num
        cont += 1
print('{} números pares foram informados. A soma é igual a {}'.format(cont, n))
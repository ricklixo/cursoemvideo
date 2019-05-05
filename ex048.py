# 048 - Faça um program que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500

# MINHA SOLUÇÃO

soma = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
        print(c, end = ' ')
print()
print('\nA Soma de todos os números é igual a {}.'.format(soma))

# SOLUÇÃO GUANABARA

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

# 051 - Programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.
# (1, 4, 7, 10, 13) a1 = 1, r = 3


# MINHA SOLUÇÃO
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
for c in range (1, 11):
    print('Termo {}: {}'.format(c, a1))
    a1 += r

# SOLUÇÃO GUANABARA
decimo = a1 + (10-1) * r
for c in range(a1, decimo + r, r):
    print('{}'.format(a1), end = ' --')
print('FIM')
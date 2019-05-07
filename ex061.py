# 061 - Refaça o exercicio 051, lendo o primeiro termo e arazão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while:

# MINHA SOLUÇÃO
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
cont = 0
while cont < 10:
    print('{}'.format(t), end = ' -> ')
    if cont == 9:
        print('FIM')
    t += r
    cont += 1

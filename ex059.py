# 059 - Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos número
# [5] Sair do programa
# O programa deverá realizar a operação solicitada em cada caso.

# MINHA SOLUÇÃO
cont = 1

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while cont !=0:
    print()
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        print('A soma entre os números {} e {} é igual a: {}'.format(n1, n2, n1+n2))
    elif opcao == 2:s
        print('A multiplicação entre os números {} e {} é igual a: {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        print('O maior número entre {} e {} é: {}'.format(n1, n2, max(n1, n2)))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        cont = 0
print('Fim do programa')

# SOLUÇÃO GUANABARA

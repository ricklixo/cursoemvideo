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
    elif opcao == 2:
        print('A multiplicação entre os números {} e {} é igual a: {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        print('O maior número entre {} e {} é: {}'.format(n1, n2, max(n1, n2)))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        cont = 0
    else:
        print('Opção inválida. Tente novamente')
print('Fim do programa')

# SOLUÇÃO GUANABARA
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Valores
    [5] Sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = n1+n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado entre {} x {} é igual a {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa.')


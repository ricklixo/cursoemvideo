# Desafio 037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base da conversão: 1 - para binário 2 - para octal 3 - para hexadecimal

escolha = 'S'
while escolha == 'S':
    num = int(input('Digite um número qualquer: '))
    opcao = int(input('Escolha a opção: \n1-Binário \n2-Octal \n3-Hexadecimal: \n'))

    if opcao == 1:
        print('O número {} convertido para Binário é igual a {}'.format(num, bin(num)))
    elif opcao == 2:
        print('O número {} convertido para Octal é igual a {}'.format(num, oct(num)))
    elif opcao == 3:
        print('O número {} convertido para Hexadecimal é igual a {}'.format(num, hex(num)))
    else:
        print('Opção inválida')
    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()

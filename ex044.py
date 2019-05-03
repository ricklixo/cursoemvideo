# DESAFIO 044 - Crie um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e a condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco = int(input('Digite o valor do produto (R$): '))
print('[1]: À vista em dinheiro ou cheque. ')
print('[2]: À vista no cartão. ')
print('[3]: em até duas vezes no cartão. ')
print('[4]: 3x ou mais no cartão. ')
pagamento = int(input('Escolha a forma de pagamento: '))


if pagamento == 1:
    preco_final = preco - (preco * 10/100)
    print('10% de desconto. de R$ {:.2f} por R$ {:.2f}'.format(preco, preco_final))
elif pagamento == 2:
    preco_final = preco - (preco * 5 / 100)
    print('5% de desconto. de R$ {:.2f} por R$ {:.2f}'.format(preco, preco_final))
elif pagamento == 3:
    parcela = int(input('Em quantas vezes deseja pagar? '))
    if parcela <= 2:
        preco_parcela = preco / parcela
        print('{} vezes de R${:.2f}'.format(parcela, preco_parcela))
        print('Sem desconto. Valor: R$ {:.2f}'.format(preco))
    else:
        print('Só são permitidos pagamentos em até 2x.')
elif pagamento == 4:
    parcela = int(input('Em quantas vezes deseja pagar? '))
    preco_final = preco + (preco * 20 / 100)
    preco_parcela = preco_final / parcela
    print('20% de juros. de R$ {:.2f} por R$ {:.2f}'.format(preco, preco_final))
    print('{} vezes de R${:.2f}'.format(parcela, preco_parcela))
else:
    print('Opção inválida.')
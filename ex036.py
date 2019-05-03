# Desafio 036 - Escreva um programa para aprovar o empréstimo bancário na compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: '))
salario = int(input('Digite o salário do comprador: '))
anos = int(input('Em quantos anos deseja parcelar? '))
anos = anos * 12
parcela = valor_casa / anos

if parcela > (salario * 30/100):
    print('Infelizmente o empréstimo não poderá ser realizado')
else:
    print('O empréstimo foi aprovado!')
    print('Valor da parcela: R$ {:.2f} mensais'.format(parcela))



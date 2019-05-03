# 034 - pergunte o salário de um funcionário e calcule o valor de seu aumento. 
# Para  salários superiores a 1,250 reais, aumento de 10%. Para inferiores, aumento de 15%

salario = float(input('Digite o salário do funcionário (R$): '))

if salario > 1250:
    ajuste = (salario * 10/100)
    aumento = ajuste + salario 
    print('O  salário é de R$ {:.2f} e seu aumento será de 10%, no total de R$ {:.2f}'.format(salario, aumento))
else:
    ajuste = (salario * 15/100)
    aumento = ajuste + salario 
    print('O  salário é de R$ {:.2f} e seu aumento será de 15%, no total de R$ {:.2f}'.format(salario, aumento))
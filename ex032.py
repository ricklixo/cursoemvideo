# 032 - Faça um programa que leia um ano qualquer e diga se é bissexto
# 1 - Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
# 2 - Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
# 3 - Pode ser que seja divisível por 400.

from datetime import date

ano = int(input('Digite um ano qualquer: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('O ano de {} é bissexto.'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))
    
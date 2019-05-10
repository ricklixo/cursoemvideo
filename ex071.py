# 071 - Crie o programa que simule o funcionamento de um caixa eletrônico.
# No inicio, pergunte o valor a ser sacado (num int) e o programa vai informar quantas cedulas de cada valor serao
# entregues. Cedulas de 50, 20, 10 e 1

# SOLUÇÃO GUANABARA - NÃO CONSEGUI FAZER
valor = int(input('Que valor você quer sacar? R$ '))

total = valor
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break

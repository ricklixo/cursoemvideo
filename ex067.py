# 067 - Faça um programa que mostre a tabuada de vários numeros, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido se o valor for negativo.


# MINHA SOLUÇÃO
while True:
    num = int(input('Digite o número o qual deseja ver a tabuada: '))
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} X {cont} = {num * cont}')
print('Tabuada encerrada')

# SOLUÇÃO GUANABARA


# 029 - Programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80km/h, mensagem dizendo que foi multado. A multa vai custar 7,00 por cada km acima do limite.

velocidade = int(input('Digite a velocidade do veículo (KM/H): '))
acima = velocidade - 80
multa = acima * 7

if velocidade > 80:
    print('O veículo está acima da velocidade em {} km/h'.format(acima))
    print('A multa será de R$ {:.2f}'.format(multa))
else:
    print('O veículo está na velocidade permitida. ')
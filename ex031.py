# 031 - Distância de uma viagem em KM. Preço da passagem 0,50 por KM até 200km e 0,45 para viagens mais longas

distancia = int(input('Digite a distância da viagem (km): '))

if distancia <= 200:
    passagem = 0.50
    preco = passagem * distancia
    print('A viagem terá a distância de {} km.'.format(distancia))
    print('O valor da passagem será de R$ {:.2f}'.format(preco))
else:
    passagem = 0.45
    preco = passagem * distancia
    print('A viagem terá a distância de {} km.'.format(distancia))
    print('O valor da passagem será de R$ {:.2f}'.format(preco))

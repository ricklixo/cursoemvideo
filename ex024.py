#024 - crie o programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'

# Minha solução:
cidade = str(input('Digite o nome de uma cidade: ')).upper().strip()

nome_cidade = cidade.split()

if nome_cidade[0] == 'SANTO':
    print('A cidade {} começa com o nome "SANTO"'.format(cidade))
else:
    print('A Cidade {} não começa com o nome "SANTO"'.format(cidade))

# Solução guanabara:
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

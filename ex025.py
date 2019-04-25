#025 - crie um programa que leia o nome de uma pessoa e digta se ela tem 'SILVA' no nome.


# MINHA SOLUÇÃO:
nome = str(input('Digite o nome de uma pessoa: ')).upper().strip()

if 'SILVA' in nome:
    print('{} possui a palavra "SILVA" em seu nome.'.format(nome))
else:
    print('{} não possui a palavra "SILVA" em seu nome.'.format(nome))

# Solução guanabara:

print('Seu nome tem Silva? {}'.format('SILVA' in nome))
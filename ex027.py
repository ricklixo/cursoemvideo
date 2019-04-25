#027 - faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente

# MINHA SOLUÇÃO:
nome = str(input('Digite um nome completo: ')).strip().title()
nomes = nome.split()
print('Primeiro nome: {}'.format(nomes[0]))
print('Último nome: {}'.format(nomes[-1]))

# SOLUÇÃO GUANABARA:

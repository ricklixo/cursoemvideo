#022 - crie um programa que leia o nome completo de uma pessoa e mostre:
'''- o nome com todas as letras maiúsculas
 - o nome com todas minúsculas
 - quantas letras ao to do (sem considerar espaços)
 - quantas letras tem o primeiro nome '''

# MINHA SOLUÇÃO
nome = str(input('Digite seu nome completo: ')).strip()

print('Nome em Maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Total de letras: {} letras'.format(len(nome)))
print('Nome sem espaços: {}'.format(nome.replace(' ', '')))
print('Total de letras (sem espaços): {} letras'.format(len(nome.replace(' ', '')))) # Ideal para remover os espaços em branco.
separa = nome.split()
print('Seu primeiro nome é {} e possui {} letras'.format(separa[0], len(separa[0]))) # Método ideal para contar.

# SOLUÇÃO GUANABARA

print('Analisando seu nome...')
print('Seu nome em maiúculas é: {}'.format(nome.upper()))
print('Seu nome em minuscúlas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # outro método para remover os espaços
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #acha o primeiro espaço dado, para verificar.

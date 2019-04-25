#026 - crie um programa que leia uma frase e moste:
'''
- quantas vezes aparece a letra 'a'
- em que posição ela aparece a primeira vez
- em que posição ela aparece pela última vez.'''

# MINHA SOLUÇÃO:
frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra "a" aparece {} vezes na frase.'.format(frase.count('A') ))
print('A Letra "a" aparece pela 1ª vez na frase no miniespaço {}'.format(frase.find('A')))
print('A Letra "a" aparece pela última vez na frase no miniespaço {}'.format(frase.rfind('A')))

# Solução Guanabara foi a mesma.
print('A letra "a" aparece {} vezes na frase.'.format(frase.count('A') ))
print('A Letra "a" aparece pela 1ª vez na frase no miniespaço {}'.format(frase.find('A') + 1)) # para não começar no 0
print('A Letra "a" aparece pela última vez na frase no miniespaço {}'.format(frase.rfind('A') + 1)) # para não começar no 0
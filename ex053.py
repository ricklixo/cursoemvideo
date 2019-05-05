# 053 - Crie um programa que leia uma frase e diga se ela é um palíndromo. Desconsidere os espaços

# MINHA SOLUÇÃO
frase = str(input('Digite uma frase: ')).strip().upper()

print('Frase normal: {}'.format(frase))
frase_espaco = frase.replace(' ', '').upper()
frase_inversa = frase_espaco[::-1]
print('Sem espaços: {}'.format(frase_espaco))
print('Invertida: {}'.format(frase_inversa))
if frase_espaco == frase_inversa:
    print('A Frase é um palíndromo.')
else:
    print('Não é um palíndromo.')

# SOLUÇÃO GUANABARA
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')

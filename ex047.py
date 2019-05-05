# 047 - Crie um programa quem ostre na tela todos os números pares que estão no intervalo entre 1 e 50

# MINHA SOLUÇÃO
for p in range(1, 51):
    if p % 2 == 0:
        print(p)
print('FIM')

# Solução guanabara
for n in range(2, 51, 2):
    print(n, end = ' ')
print('\nAcabou')


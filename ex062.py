# 062 - Melhore  desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra que quer mostrar 0 termos.

# MINHA SOLUÇÃO - na verdade não entendi direito como fiz, mas ficou certo
cont = 0
termos = 10
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
while termos != 0:
    while cont < termos:
        print('{}'.format(t), end = ' -> ')
        if cont == (termos - 1): # essa parte sempre mostra o "fim" no local certo, já que o ultimo termo nao aparece
            print('FIM')
        t += r
        cont += 1
    termos = int(input('Quantos termos a mais deseja inserir? '))
    cont = 0

# SOLUÇÃO GUANABARA

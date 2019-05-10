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
    termos = int(input('Quantos termos a mais deseja mostrar? '))
    cont = 0

# SOLUÇÃO GUANABARA
print('Gerador de PA')
print()
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da Pa: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos a mais? '))
print('Termos mostrados: {}'.format(total))
print('FIM')


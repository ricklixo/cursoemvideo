# Desafio 02 - Crie um script que leia o dia, o mes e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

nome = str(input("Digite seu nome: "))
dia = int(input("Digite o dia em que você nasceu: "))
mes = int(input("Digite o mês em que você nasceu (1 ao 12): "))
ano = int(input("Digite o ano em que você nasceu: "))
idade = (2019 - ano)

print("Olá {0}, bem vindo! Você nasceu em {1}/{2}/{3} e possui {4} anos.".format(nome, dia, mes, ano, idade))
# 035 - leia o comprimento de 3 retas e dizer se podem ou não formar um triangulo (principio matemático sobre formulação de triangulo)
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

a = int(input('Digite o comprimento da reta 01: '))
b= int(input('Digite o comprimento da reta 02: '))
c = int(input('Digite o comprimento da reta 03: '))

if ((b - c) < a < (b + c) or (a - c)< b < (a + c) or (a - b) < c < (a + b)):
    print('É possível formar um triangulo')
else:
    print('Não é possível formar um triangulo')

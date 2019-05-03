# Desafio 042 - 035 - leia o comprimento de 3 retas e dizer se podem ou não formar um triangulo (principio matemático sobre formulação de triangulo)
#Refaça o desafio 035 e acrescente o recurso de mostrar que tipo de triangulo será formado
# -Equilatero: todos os lados iguais
# -Isosceles: dois lados iguais
# -Escaleno: todos os lados diferentes

# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

a = int(input('Digite o comprimento da reta 01: '))
b= int(input('Digite o comprimento da reta 02: '))
c = int(input('Digite o comprimento da reta 03: '))

if ((b - c) < a < (b + c) or (a - c)< b < (a + c) or (a - b) < c < (a + b)):
    if a == b and b == c:
        print('É possível formar um triangulo, e ele será Equilátero.')
    elif a == b or a == c or c == b:
        print('É possível formar um triangulo, e ele será Isósceles.')
    elif a != b and a != c and b != c:
        print('É possível formar um triangulo, e ele será Escaleno.')
else:
    print('Não é possível formar um triangulo')

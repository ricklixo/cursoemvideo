# 018 - Leia um ângulo qualquer e mostre seu seno, cosseno e tangente.

from math import cos, sin, tan, radians

angulo = float(input('Digite um ângulo qualquer: '))

ang = radians(angulo)
print('SENO: {:.3f}'.format(sin(ang)))
print('COSSENO: {:.3f}'.format(cos(ang)))
print('TANGENTE: {:.3f}'.format(tan(ang)))

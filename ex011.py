#Desafio 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura

tinta = area / 2

print('A parede tem a dimensão de {} x {} m². \nSua área total é de {} m²'.format(largura, altura, area))

print('Para pintar essa área, são necessários {:.1f} litros de tinta'.format(tinta))


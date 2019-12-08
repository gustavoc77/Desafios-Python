# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o  comprimento da hipotenusa.

from math import hypot

co = float(input('O compruento do cateto oposto: '))
ca = float(input('O comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))


hi = math.hypot(co, ca)
print('Hipotenusa vai medir {:.2f}'.format(hi))

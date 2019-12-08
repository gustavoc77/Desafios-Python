# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import time
from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo: '))
print('...........CALCULANDO.........')
loop = 0
time.sleep(1.2)
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('''O ângulo de {}º
         tem o SENO de {:.2f}º
         o COSSENO de {:.2f}º
         e a TANGENTE de {:.2f}º
                        '''.format(angulo,seno,cosseno,tangente))

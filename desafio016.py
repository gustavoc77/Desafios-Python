# crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import floor
numero = float(input('Digite um número qualquer: '))
numero_inteiro = floor(numero)
print(numero_inteiro)
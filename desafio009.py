# faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
numero = int(input('Digite um número para ver sua tabuada: '))
for i in range(11):
    print('{} x {} = {}'.format(numero, i,numero*i))
# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

print('ORDEM DE APRESENTAÇÃO DOS TRABALHOS')
nome1 = input('Digite o nome: ')
nome2 = input('Digite o nome: ')
nome3 = input('Digite o nome: ')
nome4 = input('Digite o nome: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('ORDEM DO SORTEIO: {}'.format(lista))

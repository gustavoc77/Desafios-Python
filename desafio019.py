# um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido

import random
import time

print('SORTEIO DE QUEM VAI APAGAR A LOUSA')
lista = ['Gustavo', 'Suellen', 'Caíne', 'Carolliny', 'Gabriel', 'Haron', 'Ricardo', 'José', 'Rafael', 'Paccas', 'Mairy', 'Karolina', 'Leonardo', 'Arthur', 'Thiago', 'Carlos', 'Alec', 'Caio', 'Lucas', 'Antonio', 'Kaique', 'Pedro']
print(lista)
print('........................SORTEANDO.....................')
loop = 0
time.sleep(1.2)
sorteio = random.choice(lista)
print('O SORTEADO FOI {}'.format(sorteio.upper()))


# Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todos as
# informações possíveis sobre ele

algo = input('Digite algo: ')
print(type(algo))
print('é alfanumérico?',algo.isalnum())
print('é do tipo decimal?',algo.isdecimal())
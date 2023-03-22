#Algortmo sorteador de sequência de apresentação
import random

print('='*20 + 'ORDEM DE APRESENTAÇÃO' + '='*20)
a = input('\nDigite o primeiro nome: ')
b = input('Digite o segundo nome: ')
c = input('Digite o terceiro nome: ')
d = input('Digite o quarto nome: ')

lista = [a,b,c,d]
random.shuffle(lista)
print(f'\nA ordem de apresentação é: {lista}')

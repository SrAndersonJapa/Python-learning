#Algoritmo de sorteio
import random
print('='*20 + 'SORTEIO' + '='*20)
a = input('\nDigite o primeiro nome: ')
b = input('Digite o segundo nome: ')
c = input('Digite o terceiro nome: ')
d = input('Digite o quarto nome: ')
lista = [a,b,c,d]

x = random.choice(lista)

print(f'\nO sorteado foi {x}!!!')

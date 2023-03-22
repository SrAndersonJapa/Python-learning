# Algoritmo que demonstra o tamanho da hipotenusa com base nos catetos
import math
print('='*20 + 'COMPRIMENTO DA HIPOTENUSA' + '='*20)
ca = float(input('\nDigite o tamanho do cateto adjacente: '))
co = float(input('Digite o tamanho do cateto oposto: '))
#hp = math.sqrt(math.pow(ca, 2) + math.pow(co, 2))
hp = math.hypot(ca, co)

print(f'\nO comprimento da hipotenusa equivale a: {hp:.2f}\n\n')

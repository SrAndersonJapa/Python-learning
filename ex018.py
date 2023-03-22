#Algoritmo que lê angulos e retorna o seno, cos e tan.
import math
print('='*20 + 'ÂNGULO -> SEN, COS, TAN' + '='*20)
a = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print(f'\nO seno de {a} é igual à: {sen:.3f}! \nO cosseno de {a} é igual à: {cos:.3f}! \nA tangente de {a} é igual à {tan:.3f}!\n\n')

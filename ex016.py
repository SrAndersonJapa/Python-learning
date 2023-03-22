#Algoritmo pára utilizar biblioteca math, demonstrando apenas a parte inteira de um número
'''import math

n = float(input('Digite um número: '))
print(f'A parte inteira do número {n} é: {math.trunc(n)}') #Truncar o número é a função q puxa a parte int
print(f'A parte inteira do número {n} é: {math.floor(n)}') #Utiliza floor força arredondar para baixo'''

n = float(input('Digite um número: '))
print(f'A parte inteira do número {n} é: {int(n)}')

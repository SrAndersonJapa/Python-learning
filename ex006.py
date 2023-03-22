#Algoritmo que mostra o dobro o triplo e a raiz de um número

x = int(input('Digite um número: '))
d = x * 2
t = x * 3
r = x ** (1/2)
print(f'O dobro de {x} é {d}. \nO triplo de {x} é {t}. \nA raiz de {x} é {r:.2f}')

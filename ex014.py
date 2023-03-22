#Algoritmo para converter grau celsius para fahrenheit

print('='*20 + 'CONVERSOR DE TEMPERATURA' + '='*20)
tc = float(input('\nQual a temperatura em graus Celsius: '))
tf = tc * 1.8 + 32

print(f'\nA temperatura em Fahrenheit equivale há: {tf:.1f}°F!\n\n')

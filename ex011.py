#Algoritmo que calcula a área de uma parede e a quantidade de tinta para pintar

print('='*20 + 'QUANTIDADE DE TINTA' + '='*20)
a = float(input('\nQual a ALTURA da parede: '))
b = float(input('Qual a LARGURA da parede: '))
c = a * b
t = c / 2 
print(f'\nPara pintar a sua parede de {c:.2f}m² será necessário {t:.2f}L de tinta!')

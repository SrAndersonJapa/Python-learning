#Algoritmo que faz o calculo de preço baseado em km rodado e dias usados

print('='*20 + 'CUSTO DO ALUGUEL' + '='*20)

km = float(input('\nQuantos km foram rodados: '))
d = float(input('Quantos dias foi utilizado: '))
p = (km * 0.15) + (d * 60)

print(f'\nO custo para {d:.0f} dias e {km:.0f} km fica no total de: R${p:.2f}\n\n')

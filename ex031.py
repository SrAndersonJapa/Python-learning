#Cálculo do preço de uma viagem

km = int(input('\n\nDigite a distância da viagem em Km: '))

if km <= 200:
    print(f'\nCusto da viagem R${km * 0.5:.2f}\n\n')
else:
    print(f'\nCusto da viagem R${km * 0.45:.2f}\n\n')

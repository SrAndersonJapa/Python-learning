# Lê um valor e caso esteja acima do limite é cobrado um outro valor baseado no tanto acima.

print('=' * 20 + 'RADAR' + '=' * 20)
vc = int(input('\nDigite a velocidade que o carro passou: '))
limite = 80 - vc

if limite < 0:
    print(f'\nVocê foi multado em R${limite * (-7)}\n\n')
print('Bom dia!')

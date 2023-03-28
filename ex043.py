#Cálculo de IMC

peso = float(input('\n\nDigite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5: 
    print(f'\n\nIMC de {imc:.2f}, está abaixo do peso!\n\n')
elif imc < 25:
    print(f'\n\nIMC de {imc:.2f}, está no peso ideal!\n\n')
elif imc < 30:
    print(f'\n\nIMC de {imc:.2f}, está com sobrepeso!\n\n')
elif imc < 40:
    print(f'\n\nIMC de {imc:.2f}, está com obesidade!!\n\n')
elif imc >= 40:
    print(f'\n\nIMC de {imc:.2f}, INDICA OBESIDADE MÓRBIDA!!!\n\n')

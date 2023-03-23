#Lê 3 números e mostra o maior e o menor

n1 = float(input('\nDigite o primeiro número: '))
maior = n1
menor = n1

n2 = float(input('Digite o segundo número: '))
if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2

n3 = float(input('Digite o terceiro número: '))
if n3 > maior: 
    maior = n3
elif n3 < menor:
    menor = n3

print(f'\nO maior número é {maior}!')
print(f'O menor número é {menor}!\n\n')

#Demonstra qual número é maior ou se são iguais

n1 = int(input('\n\nDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('\nO primeiro valor é maior!\n\n')
elif n2 > n1:
    print('\nO segundo valor é maior!\n\n')
elif n1 == n2:
    print('\nNenhum é maior, pois os valores são iguais!\n\n')

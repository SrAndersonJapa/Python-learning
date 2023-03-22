#Máquina escolhe um número de 0 à 5 e usuário tenta adivinhar
import random

n = random.randint(0,5)
print('='*20 + 'JOGO DA ADIVINHAÇÃO' + '='*20)
x = str(input('\nPensei em um número entre 0 e 5. Gostaria de tentar adivinhar? Digite (s) ou (n): ').upper().strip())
if x == 'S':
    y = int(input('\nDigite o número: '))
    if y == n: 
        print('\nPARABÉNS ACERTOU!!')
    else:
        print(f'\nERROU PERDEU! O número correto era {n}!')
else:
    print('\nQue pena!\n\n')

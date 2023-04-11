# Máquina escolhe um número randomico e o usuário digita um número até adivinhar;

import random

n = random.randint(1, 10)

print('=' * 20)
print('JOGO DA ADIVINHAÇÃO')
print('=' * 20)

rp = 0
while rp != 1:
    inicio = str(input(
        '\nPensei em um número entre 1 e 10. Gostaria de tentar adivinhar?\n[S/N] - ').strip().upper())
    if inicio == 'S' or inicio == 'N':
        rp = 1
    else:
        print('RESPOSTA INVÁLIDA!')

if inicio == 'S':
    c = 0
    cont = 1
    while c != 1:
        n2 = int(input('\n\nDigite o número que você acha que eu pensei: '))
        if n == n2:
            print(f'\n\nVocê acertou! Foram apenas {cont} tentativas!\n\n')
            c = 1
        else:
            print('\nVocê errou, tente novamente!')
            cont += 1

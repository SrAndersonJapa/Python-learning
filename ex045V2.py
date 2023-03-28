#Versão do professor;
import random
import time
itens = ('Pedra' , 'Papel', 'Tesoura')
computador = random.randint(0,2)

print('\nSUAS OPÇÕES:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA\n')

jogador = int(input('Qual a sua jogada? - '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)

if jogador < 0 or jogador > 2:
    print('JOGADA INVÁLIDA')
elif computador == 0:
    print('-=' * 15)
    print(f'\nComputador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}\n')
    print('-=' * 15)
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif computador == 1:
    print('-=' * 15)
    print(f'\nComputador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}\n')
    print('-=' * 15)
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif computador == 2:
    print('-=' * 15)
    print(f'\nComputador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}\n')
    print('-=' * 15)
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')

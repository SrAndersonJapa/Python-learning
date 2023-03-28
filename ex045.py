#Pedra, papel e tesoura;
import random

print('-=-' * 20)
pc = ('PEDRA PAPEL TESOURA')
print(f'{pc:^60}')
print('-=-' * 20)
pc = pc.split()

dic = {"PEDRA":1, "PAPEL":2, "TESOURA":3}

print('\n\nESCOLHA UMA OPÇÃO PARA JOGAR COMIGO!')
print('\n\n1- PEDRA!')
print('2- PAPEL!')
print('3- TESOURA!\n\n')
us = int(input('OPÇÃO: '))

if us == 1:
    opu = ('PEDRA')
elif us == 2:
    opu = ('PAPEL')
elif us == 3:
    opu = ('TESOURA')
else:
    print('\n\nOPÇÃO INVÁLIDA\n\n')
    exit(0)

opc = random.choice(pc)
opcd = dic[opc]
opud = dic[opu]

if opud == opcd:
    print(f'EMPATAMOS, você escolheu {opu} e eu escolhi {opc}!')
elif opud < opcd and opcd - opud != 2:
    print(f'Você escolheu {opu} e eu escolhi {opc}, portanto você perdeu!')
elif opud == 1 and opcd == 3:
        print(f'Você escolheu {opu} e eu escolhi {opc}, portanto você ganhou!')
elif opud > opcd and opud - opcd != 2:
    print(f'Você escolheu {opu} e eu escolhi {opc}, portanto você ganhou!')
elif opud == 3 and opcd == 1:
    print(f'Você escolheu {opu} e eu escolhi {opc}, portando você perdeu!')

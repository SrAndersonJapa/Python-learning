#Versão do professor
from random import randint
import time

computador = randint(0, 5) #Faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
time.sleep(3)
if jogador == computador:
    print('\nPARABÉNS! Você conseguiu me vencer!\n\n')
else:
    print(f'\nGANHEI! Eu pensei no número {computador} e não no {jogador}!\n\n')

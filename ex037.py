#Conversor de números int para binário, octal ou hexadecimal

n = int(input('\n\nDigite o número int que você quer converter: '))
print('\nConverter para binário       digite 1')
print('Converter para octal         digite 2')
print('Converter para hexadecimal   digite 3\n\n')

op = int(input('OPÇÃO: '))

if op == 1:
    print(f'O valor convertido de {n} em binário é {bin(n)[2::]}')
elif op == 2:
    print(f'O valor convertido de {n} em octal é {oct(n)[2::]}')
elif op == 3:
    print(f'O valor convertido de {n} em hexadecimal é {hex(n)[2::]}')
else:
    print('OPÇÃO INVÁLIDA! ADEUS!')
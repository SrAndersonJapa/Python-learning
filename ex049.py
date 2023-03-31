# Tabuada;

n = int(input('\nDigite o número que você quer a tabuada: '))
vz = int(input('\nDigite até quanto você quer a tabuada: '))

for c in range(0, vz + 1):
    if c >= 10:
        print(f'{n} x  {c} =  {n*c}')
    else:
        print(f'{n} x   {c} =  {n*c}')

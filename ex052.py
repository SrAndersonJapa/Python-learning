#Lê um número e fala se é primo ou não;

n = int(input('\nDigite um número: '))
c2 = 0
d = 0 

if n < 2:
    print('\nNão é primo!\n')
    exit(0)
else:
    for c in range (1, n+1):
        d = n % c
        if d == 0:
            c2 += 1
            if c2 > 2:
                print(f'\n{n} não é um número primo!\n')
                exit(0)
if c2 == 2:
    print(f'\nO número {n} é um número primo!\n')

# Lê um n pergunta se deseja continuar, mostra o maior o menor e a média;

c = 0
c2 = 0
maior = 0
menor = 0
s = 0
while c < 1:
    c3 = False
    cont = 'F'
    n = int(input('\n\nDigite um número: '))
    s += n
    c2 += 1
    if c2 == 1:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    cont = str(input('\n\nDeseja continuar?[S/N]: ')).upper()
    while c3 != True:
        if cont == 'N':
            c = 1
            c3 = True
        elif cont == 'S':
            c3 = True
        elif cont != 'S' or cont != 'N':
            print('\n\nRESPOSTA INCORRETA!\n\n')
            cont = str(input('\n\nDeseja continuar?[S/N]: ')).upper()
media = s / c2
print(f'\n\nMAIOR NÚMERO: {maior}')
print(f'MENOR NÚMERO: {menor}')
print(f'MÉDIA DOS NÚMEROS: {media:.2f}\n\n')

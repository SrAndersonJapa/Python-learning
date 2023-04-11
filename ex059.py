#Recebe 2 números e demonstra um menu com opções;

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

op = 0
sm = 0

while op != 5:
    print('\n[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR NÚMERO')
    print('[4] DIGITAR NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    op = int(input('\n\nDigite a opção desejada: '))
    if op == 1:
        sm = n1 + n2
        print(f'\n\nA soma dos números é {sm:.2f}!\n\n')
    elif op == 2:
        sm = n1 * n2
        print(f'\nO resultado da multiplicação dos números é {sm:.2f}!\n\n')
    elif op == 3:
        if n1 > n2:
            print(f'\n\nO maior número é {n1}!\n\n')
        elif n2 > n1:
            print(f'\n\nO maior número é {n2}!\n\n')
        elif n1 == n2:
            print('\n\nOs dois números tem valor igual!\n\n')
    elif op == 4:
        n1 = float(input('\n\nDigite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif op < 1 or op > 5:
        print('\n\nOPÇÃO INVÁLIDA!\n\n')

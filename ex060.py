# Fatorial de um número;
# Existe uma função para factorial na biblioteca math;

n = int(input('\n\nDigite um número: '))
n2 = n
ft = n
c = n - 1
n2 = n2 - 1

if n == 0:
    print('O fatorial de 0 é: 1')
    exit(0)
elif n < 0:
    print('Não se calcula fatorial de número negativo!')
    exit(0)
else:
    while c > 0:
        ft = ft * n2
        c = c - 1
        n2 = n2 - 1

print(f'\n\nO fatorial de {n} é: {ft}\n\n')

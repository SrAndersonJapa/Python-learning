# Soma n int pares e desconsidera os impares
s = 0
for c in range(1, 7):
    n = int(input(f'Digite o número {c}: '))
    if n % 2 == 0:
        s += n
print(f'\n\nA soma dos pares é: {s}\n\n')

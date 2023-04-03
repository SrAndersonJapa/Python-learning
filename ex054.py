# Lê a idade de 7 pessoas e determina quantas são maiores de idade;

c2 = 0
c3 = 0

for c in range(1, 8):
    idade = int(input(f'\nDigite a idade da pessoa nº{c}: '))
    if idade >= 21:
        c2 += 1
    else:
        c3 += 1
print(f'\n\n{c2} pessoas já são maiores de idade!\n\n')
print(f'\n\n{c3} pessoas ainda não são maiores de idade!\n\n')

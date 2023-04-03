#Lê o peso de 5 pessoas e fala qual o maior e qual o menor;

maiorp = 0
menorp = 0

for c in range(1,6):
    peso = float(input(f'\nDigite o peso nº{c}: '))
    if c == 1:
        maiorp = peso
        menorp = peso
    if peso > maiorp:
        maiorp = peso
    elif peso < menorp:
        menorp = peso

print(f'\n\nMAIOR PESO: {maiorp}kg!!')
print(f'MENOR PESO: {menorp}kg!!\n\n')

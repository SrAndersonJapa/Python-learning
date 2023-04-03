# Pega alguns dados e faz algumas análises;

ivelho = 0
cmnova = 0
s = 0
nvelho = 'vazio'

for c in range(1, 5):
    nome = str(input(f'\n\nDigite o {c}º nome: ')).strip()
    idade = int(input(f'Digite a {c}ª idade: '))
    sexo = str(input('Digite o sexo M(masculino) ou F(feminino): ')).upper()
    s += idade
    if sexo == 'M':
        if idade > ivelho:
            ivelho = idade
            nvelho = nome
    elif sexo == 'F':
        if idade < 20:
            cmnova += 1
media = s / 4
if nvelho != 'vazio':
    print(f'\n\nO homem mais velho é {nvelho}, com {ivelho} anos!')
else: 
    print('\n\nNão há homens registrados!')
print(f'Há {cmnova} mulheres com menos de 20 anos!')
print(f'A média da idade das 4 pessoas é: {media:.2f} anos!\n\n')

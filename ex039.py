#Vê a data de nascimento e fala se está no ano de se alistar
import datetime

d1 = datetime.date.today().day
m1 = datetime.date.today().month
y1 = datetime.date.today().year

dia = int(input('\nDia do nascimento: '))
mes = int(input('Mês do nascimento: '))
ano = int(input('Ano do nascimento: '))

if y1 - ano < 17:
    tempo = 18 + (ano - y1)  
    print(f'\n\nAinda faltam {tempo} ano/anos!')
elif y1 - ano == 17:
    if mes < 7:
        print('\n\nVocê faz 18 até metade do ano, então deve se alistar!')
    else:
        print('\n\nSeu alistamento deve ser feito ano que vem!')
elif y1 - ano == 18:
    print('\n\nVocê tem 18 portando deve se alistar!')
else:
    idade = y1 - ano
    tempo = idade - 18
    print(f'\n\nVocê tem {idade} anos então já se passaram {tempo} anos de se alistar!!')

print(f'\n\nNASCIMENTO: {dia}/{mes}/{ano}')
print(f'DATA DE HOJE: {d1}/{m1}/{y1}\n\n')

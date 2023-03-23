# Vê se o ano é bissexto
import datetime

print('=' * 20 + 'LEITOR DE ANO BISSEXTO' + '=' * 20)

ano = int(input('\nDigite o ano: '))
if ano == 0:
    ano = datetime.date.today().year
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'\n{ano} É UM ANO BISSEXTO!\n\n')
        else:
            print(f'\n{ano} NÃO É BISSEXTO!\n\n')
    else:
        print(f'\n{ano} É UM ANO BISSEXTO!\n\n')
else:
    print(f'\n{ano} NÃO É BISSEXTO!\n\n')

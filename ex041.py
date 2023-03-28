# Lê o ano de nascimento e categoriza
import datetime

nas = int(input('\nDigite o ANO de nascimento: '))
ano = datetime.date.today().year
idade = ano - nas

if idade < 0:
    print('\n\nIDADE INCORRETA!\n\n')
elif idade < 9:
    print('\n\nCATEGORIA MIRIM!\n\n')
elif idade < 14:
    print('\n\nCATEGORIA INFANTIL!\n\n')
elif idade < 19:
    print('\n\nCATEGORIA JUNIOR!\n\n')
elif idade == 19 or idade == 20:
    print('\n\nCATEGORIA SENIOR!\n\n')
elif idade > 20:
    print('\n\nCATEGORIA MASTER!\n\n')

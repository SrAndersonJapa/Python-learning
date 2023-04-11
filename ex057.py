#Lê o sexo até que a resposta seja m ou f;

rp = 0
#rp2 = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
#while rp2 not in 'MF':
#    rp2 = str(input('RESPOSTA INVÁLIDA. Digite o seu sexo [M/F]: ')).strip().upper()

while rp != 1:
    rp2 = str(input('\nDigite o seu sexo [M/F]: ')).strip().upper()
    if rp2 == 'M' or rp2 == 'F':
        rp = 1 
    else:
        print('\nRESPOSTA INVÁLIDA! DIGITE NOVAMENTE!')
if rp2 == 'M': 
    print('\n\nEntão você é do sexo masculino!\n\n')
elif rp2 == 'F':
    print('\n\nEntão você é do sexo feminino!\n\n') 

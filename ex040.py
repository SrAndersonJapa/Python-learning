#Lê 2 notas, calcula a média e fala se foi aprovado ou não;

print('-=-' * 20)
media = 'MÉDIA'
print(f'{media:^60}')
print('-=-' * 20)

n1 = float(input('\n\nDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
    print('\n\nVALORES DIGITADOS ESTÃO ERRADOS INICIE DE NOVO!\n\n')
elif media < 5:
    print(f'\n\nMédia: {media:.2f} - REPROVADO!!\n\n')
elif media >= 5 and media <= 6.9:
    print(f'\n\nMédia: {media:.2f} - RECUPERAÇÃO!\n\n')
elif media >= 7:
    print(f'\n\nMédia: {media:.2f} - APROVADO, PARABÉNS!!\n\n')

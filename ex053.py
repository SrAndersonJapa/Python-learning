# Lê uma frase e fala se é ou não palindromo;

frase = str(input('\n\nDigite uma frase: ')).upper().split()
frase = ''.join(frase)
c2 = len(frase)
flista = ' '.join(frase)
flista = flista.split()
flista2 = []
flista3 = []

for c in range(c2, 0, -1):
    flista2 = flista[c-1]
    flista3 += flista2
flista3 = ''.join(flista3)

if frase == flista3:
    print('\n\nA frase é um palindromo!\n\n')
else:
    print('\n\nA frase não é um palindromo!!\n\n')

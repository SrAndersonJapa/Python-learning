#Ver se é possível as retas formarem um triângulo e qual dos 3 tipos elas formam

r1 = float(input('\n\nDigite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

s1 = r1 + r2
s2 = r2 + r3
s3 = r3 + r1

if s1 > r3 and s2 > r1 and s3 > r2:
    if r1 == r2 == r3:
        print('\n\nTRIÂNGULO EQUILÁTERO!\n\n')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('\n\nTRIÂNGULO ISÓSCELES!\n\n')
    else:
        print('\n\nTRIÂNGULO ESCALENO!\n\n')
else:
    print('\n\nAS RETAS NÃO FORMAM UM TRIÂNGULO!\n\n')

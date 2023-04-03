#Mostra os 10 primeiros termos de uma PA;

pt = int(input('\nDigite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
s = pt

for c in range(0,10):
    print(s)
    s = s + r

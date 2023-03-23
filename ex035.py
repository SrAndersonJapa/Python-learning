#Verifica o valor de 3 retas e fala se pode ou não formar um triângulo
print('-=' * 20)
print('ANALISANDO TRIÂNGULO')
print('-=' * 20)

r1 = float(input('\nDigite o valor da reta 1: '))
r2 = float(input('Digite o valor da reta 2: '))
r3 = float(input('Digite o valor da reta 3: '))

mod1 = abs(r1 - r2)
sm1 = r1 + r2
mod2 = abs(r1 - r3)
sm2 = r1 + r3
mod3 = abs(r2 - r3)
sm3 = r2 + r3

if mod1 < r3 < sm1:
    if mod2 < r2 < sm2:
        if mod3 < r1 < sm3:
            print('\nAs medidas formam um triângulo!\n\n')
else:
    print('\nAs medidas não formam um triângulo!\n\n')

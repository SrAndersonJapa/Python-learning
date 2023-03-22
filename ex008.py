#Converter metro p/ cm e mm

print('='*20 + 'CONVERSOR DE M -> cm e mm' + '='*20)

m = float(input('\nDigite quantos metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'\n\n{m}m equivalem à:') 
print(f'\n{km}km \n{hm}hm \n{dam}dam \n{dm:.0f}dm \n{cm:.0f}cm \n{mm:.0f}mm\n')

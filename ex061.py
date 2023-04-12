# Progressão aritmética com while;

pt = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
pa = pt
c = 0

while c < 10:
    print(pa)
    pa = pa + rz
    c += 1

#Igual 62, porém o usuário pode pedir mais termos;

pt = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
pa = pt
c = 0

while c < 10:
    print(pa)
    pa += rz
    c += 1

teste = True

while teste == True:
    termos = int(input('Digite quantos termos a mais gostaria de ver: '))
    if termos > 0:
        for cont in range(termos, 0, -1):
            print(pa)
            pa += rz
    else:
        teste = False

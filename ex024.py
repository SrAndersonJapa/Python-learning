#Algoritmo que vê se a string começa com determinada palavra

cd = str(input('Digite o nome da cidade: ').upper())
x = cd.split()
teste = x[0]
print(f'O nome da cidade começa com SANTO - {bool(teste.count("SANTO",0,5))}!')

#cd = str(input('Digite o nome da cidade: ').strip())
#print(cd[:5].upper() == 'SANTO')

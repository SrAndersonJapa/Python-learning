#Algoritmo que le um nome e diz se tem Silva no nome

#nome = str(input('Digite o seu nome completo: ').upper())
#print(f'Seu nome contém SILVA - {bool(nome.count("SILVA"))}')

nome = str(input('Digite o seu nome completo: ').strip())
print(f'Seu nome tem Silva - {"SILVA" in nome.upper()}!')

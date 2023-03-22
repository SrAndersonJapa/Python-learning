#Algoritmo que lê um nome completo e demonstra informações de str sobre ele.
print('-'*20 + 'ANALISADOR DE NOMES' + '-'*20)
nome = str(input('\nDigite o seu nome completo: ').strip())
print(f'\nNome em maiúsculo: {nome.upper()}')
print(f'Nome em minúsculo: {nome.lower()}')

#print(f'Quantidade de letras: {len(nome) - nome.count(" ")}')

x = nome.split()
y = x[0]
x = ''.join(x)
print(f'Seu nome possui {len(x)} letras!')
print(f'O primeiro nome possui {len(y)} letras!\n\n')

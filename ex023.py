#Le um número de 0 à 9999 e mostra o digito separado na tela
#Não dá pra fazer sem estruturas de repetição

'''n = input('Digite um número entre 0 e 9999: ')
n = ' '.join(n)
n = n.split()
print('Unidade:', n[3])
print('Dezena:', n[2])
print('Centena:', n[1])
print('milhar:', n[0])'''

# // Divisão inteira retornando o número desconsiderando td dps da virgula + % resto da divisão por algum número retornando apenas o resto que no exercício significa o digito a ser mostrado.
n2 = int(input('Digite um número entre 0 e 9999: '))
u = n2 // 1 % 10
d = n2 // 10 % 10
c = n2 // 100 % 10
m = n2 // 1000 % 10 
print(f'\n\nUnidade: {u}')
print(f'Dezena: {d}')
print(f'Centeza: {c}')
print(f'Milhar: {m}\n')

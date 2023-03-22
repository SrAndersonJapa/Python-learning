# Algoritmo que lê um nome e prionta o primeiro e último nome.

nome = str(input('\nDigite o seu nome: '))
n = nome.split()
x = n[0]
print(f'\n\nSeu primeiro nome é {x}!')
# n1 = n[::-1] - Com fatiamento tb funciona 2 pontos vazios para percorrer toda a lista e -1 pra ir de trás pra frente.
n1 = list(reversed(n))
y = n1[0]
#print(f'Seu último nome é {nome[len(nome)-1]}') Tb funciona 
print(f'Seu último nome é {y}!\n\n')

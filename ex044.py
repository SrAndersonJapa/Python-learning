#Verifica condições de pagamento e retorna valor com desconto ou juros;
print('-=-' * 20)
print(f'{"PAGAMENTO":^60}')
print('-=-' * 20)

preço = float(input('\nDigite o valor do produto: '))
print('\nESCOLHA ENTRE AS OPÇÕES DE PAGAMENTO ABAIXO:')
print('\n1- À vista, dinheiro/cheque!')
print('2- À vista, no cartão!')
print('3- Até 2x no cartão!')
print('4- 3x ou mais no cartão!\n')
op = int(input('OPÇÃO: '))

if op == 1:
    preço = preço * 0.9
    print(f'\n\nÀ vista no dinheiro ou cheque o valor total fica em R${preço:.2f}!\n\n')
elif op == 2:
    preço = preço * 0.95
    print(f'\n\nÀ vista no cartão o valor total fica em R${preço:.2f}!\n\n')
elif op == 3:
    print(f'\n\nEm até 2x no cartão o preço é o mesmo - R${preço:.2f}!\n\n')
elif op == 4:
    preço = preço * 1.2
    vz = int(input('Em quantas vezes será parcelado? - '))
    pc = preço/vz 
    print(f'\n\nNo cartão o preço total fica em R${preço:.2f}!')
    print(f'Em {vz} parcelas, cada parcela fica no valor de R${pc:.2f}\n\n')
else:
    print('\n\nOPÇÃO INVÁLIDA!\n\n')

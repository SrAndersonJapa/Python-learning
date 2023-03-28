# Cálcula se o Valor de empréstimo pode ser realizado, utilizando if else;

print('=-=' * 20)
p = 'EMPRÉSTIMO!!'
print(f'{p:^60}')
print('=-=' * 20)

casa = float(input('\nDigite o valor da casa: R$'))
sal = float(input('Digite o salário do comprador: R$'))
anos = int(input('Digite em quantos ANOS será pago: '))
print('=-=' * 20)
pmes = casa / (anos * 12)
psal = sal * 0.3

if pmes > psal:
    print('\n\nEMPRÉSTIMO NEGADO!!\n\n')
    print(f'Para o salário de R${sal} a parcela pode ser no máximo R${psal:.2f} por mês!')
    print(f'A parcela da casa em {anos} anos fica no valor de R${pmes:.2f} por mês!\n\n')
else:
    print('\n\nEMPRÉSTIMO APROVADO!!\n\n')
    print(f'A parcela em {anos} anos fica no valor de R${pmes:.2f} por mês!!\n\n')

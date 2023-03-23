# Cálculo de aumento baseado em um valor teto.
print('=' * 20 + 'AUMENTO DE SALÁRIO' + '=' * 20)
sal = float(input('\nDigite o valor do salário: '))

if sal > 1250:
    print(f'\nO salário de R${sal} passa a ser R${sal * 1.1:.2f}!\n\n')
else:
    print(f'\nO salário de R${sal} passa a ser R${sal * 1.15:.2f}!\n\n')

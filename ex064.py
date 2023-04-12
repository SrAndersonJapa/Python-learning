# Lê números inteiros até o usuário digitar 999;

print('\n\nDigite [999] caso queira sair do programa!\n\n')

n = 0
s = 0
qn = 0
n = int(input('Digite um número inteiro: '))
while n != 999:
    s = s + n
    qn += 1
    n = int(input('Digite um número inteiro: '))
print(f'\n\nForam digitados {qn} números e a soma deles resultam em {s}!\n\n')

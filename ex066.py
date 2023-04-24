# Lê números até a condição do break, demonstra quantos foram e a soma;
tit = 'DIGITE NÚMEROS'
print(f'{tit:-^60}')
c = 0
s = 0
while True:
    n = int(input('\nDigite um número(999 finaliza): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'\n\nForam digitados {c} números e a soma deles é {s}\n\n')

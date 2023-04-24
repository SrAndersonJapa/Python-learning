#Demonstra a tabuada até o usuário digitar um n negativo;

while True:
    n = int(input('Digite a tabuada que você quer ver: '))
    if n < 0:
        break
    print('-' * 40)
    for c in range(1,11):
        r = n * c
        if c == 10:
            print(f'{n} x {c} = {r}')
        else:
            print(f'{n} x  {c} = {r}')
    print('-' * 40)
print('ATÉ A PRÓXIMA!!')

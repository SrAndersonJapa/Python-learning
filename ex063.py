# Sequência de Fibonacci com while;

n = int(input('\n\nDigite quantos termos de fibonacci você quer ver: '))
fb = 0
fb1 = 1
fb3 = 0


if n == 1:
    print('0')
    exit(0)
elif n == 2:
    print('0')
    print('1')
    exit(0)
elif n <= 0:
    print('Valor errado!')
    exit(0)

print('0')
print('1')
n = n - 2

while n > 0:
    fb3 = fb + fb1
    fb = fb1
    fb1 = fb3
    print(fb3)
    n -= 1

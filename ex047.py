# Mostra os números pares entre 1 e 50
print('NÚMEROS PARES ENTRE 1 E 50!')
for c in range(1, 51):
    if c % 2 == 0:
        print(c)

#ou
#segunda solução gasta menos processo;

for c in range(2, 52, 2):
    print(c)

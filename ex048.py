#Faz soma dos divisiveis por 3 entre 1 e 500 que são impares;

s = 0
for c in range(1,501,2):
    if c % 3 == 0:
        s += c
print(s)

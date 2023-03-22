# Algoritmo que analisa a letra A em str

f = str(input('Digite algo: ').upper().strip())
print(f'\nA letra A aparece {f.count("A")} vezes!')
print(f'A letra A aparece a primeira vez na posição {f.find("A")+1}!')
print(f'A letra A aparece a ultima vez na posição {f.rfind("A")+1}!')
 
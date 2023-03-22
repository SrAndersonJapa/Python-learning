# script que fala o tipo primitivo do texto digitado e da informações sobre o que representa o texto.
# Tipos primitivos: int, float, bool, str.

x = input('Digite algo: ')
print('O tipo primitivo do texto digitado é', (type(x)))
print(f'O texto digitado é alfanumérico - {x.isalnum()}')
print(f'O texto digitado é somente letra - {x.isalpha()}')
print(f'O texto digitado é um número decimal - {x.isdecimal()}')
print(f'O texto digitado está escrito em letra minúscula - {x.islower()}')
print(f'O texto digitado é somente número - {x.isnumeric()}')
print(f'O texto digitado está escrito em letra maiúscula - {x.isupper()}')
print(f'O texto digitado é um indentificador - {x.isidentifier()}')
print(f'O texto digitado é um digito - {x.isdigit()}')
print(f'O texto digitado contém somente espaços - {x.isspace()}')
print(f'O texto pode ser impresso - {x.isprintable()}')
print(f'O texto começa com maiúscula e termina com minúscula (capitalizado) - {x.istitle()}')

# x = int(input('Digite um número: '))
# print(type(x))

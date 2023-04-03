# Versão do professor;

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

#posição é igual o tamanho da str -1, até -1 pra chegar em 0, de -1 em -1 que significa de trás pra frente;
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

#Segunda forma, a lista percorre do inicio ao fim de trás pra frente. E testa com o if;
#inverso = junto[::-1]

if inverso == junto:
    print('É palindromo!')
else:
    print('Não é palindromo!')

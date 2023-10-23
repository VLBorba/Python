frase = input('Digite uma frase e veremos se é um palíndromo: ').strip().lower()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
if inverso == junto:
    print('Está frase é \033[1;32msim\033[m um palíndromo!')
else:
    print('Está frase \033[1;31mnão\033[m é um palíndromo.')

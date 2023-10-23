tupla = ('Zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
          'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    number = int(input('Digite um valor entre 0 e 20: '))
    while number < 0 or number > 20:
        number = int(input('Tente novamente. Digite um valor entre 0 e 20: '))
    print(f'\033[1;7m {number} por extenso é {tupla[number]}.\033[m')
    continuar = input('Quer ver outro valor? ').lower().strip()[0]
    while continuar not in 'sn':
        continuar = input('Tente novamente. Quer ver outro valor? ').lower().strip()[0]
    if continuar[0] == 'n':
        break
print('Obrigao pela preferência!')

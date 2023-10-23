maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input('Digite o peso da {}ºPessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Pessoa mais \033[1;33mleve\033[m tem {}Kg'.format(menor))
print('Pessoa mais \033[1;31mpesada\033[m tem {}Kg'.format(maior))

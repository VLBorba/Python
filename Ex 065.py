soma = 0
cont = 1
valor = int(input('Digite um valor: '))
continuar = str(input('Você deseja continuar? ')).lower().split()[0]
soma += valor
maior = menor = valor
while continuar in 'sim':
    valor = int(input('Digite um valor: '))
    soma += valor
    cont += 1
    média = soma / cont
    if cont == 1:
        valor = maior = menor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    continuar = str(input('Você deseja continuar? ')).lower().split()[0]
print(f'Maior valor é \033[1;35m{maior}\033[m')
print(f'Menor valor é \033[1;33m{menor}\033[m')
if cont == 1:
    print('Sua média é \033[1;4m{}.'.format(valor))
else:
    print('A média de valores digitados foi \033[1;4m{:.2f}'.format(média))

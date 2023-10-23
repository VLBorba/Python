gasto = mil = menor = cont = 0
menornome = ' '
while True:
    nome = input('Digite o nome do produto: ')
    preço = float(input('Digite o preço do produto: $'))
    cont += 1
    gasto += preço
    if preço > 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        menornome = nome
    continuar = ' '
    while continuar[0] not in 'sn':
        continuar = input('Deseja continuar? ').lower().split()[0]
    if continuar[0] == 'n':
        break
print(f'Total gasto em produtos foi \033[1;4;36m{gasto}\033[m')
print(f'Total de produtos acima de r$ 1000,00 foram \033[1;4;37m{mil}\033[m')
print(f'O nome do produto mais barato é: \033[1;4;33m{menornome} e custa {menor}\033[m')

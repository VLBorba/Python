cont = n = soma = 0
print('~'*31)
print('\033[1;36mDigite 999 para sair do gerador\033[m')
print('~'*31)
n = int(input('Digite um valor: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um valor: '))
print('foram digitados \033[1;4m{} Valores.\033[m'.format(cont))
print('A soma de todos os valores digitados é \033[1;35m{}\033[m.'.format(soma))

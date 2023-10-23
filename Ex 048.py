soma = 0
valores = 0
for impar in range(1,500,2):
    if impar % 3 == 0:
        soma = soma + impar
        valores = valores + 1
print('A soma dos valores é \033[1;7;40m{}\033[m'.format(soma))
print('A quantidade de números \033[1;4m{}\033[m'.format(valores))

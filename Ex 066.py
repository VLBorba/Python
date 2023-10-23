s = cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos {cont} valores é: \033[1;4m{s}\033[m')

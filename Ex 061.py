primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
n = primeiro
cont = 1
while cont <= 10:
    print(n, end='-> ')
    n += razão
    cont += 1
print('FIM.')

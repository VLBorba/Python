primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
n = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(n, end='-> ')
        n += razão
        cont += 1
    print('\n')
    mais = int(input('Quantos termos a mais você quer? '))
print(f'Foram mostrados {total} Termos')
print('FIM.')

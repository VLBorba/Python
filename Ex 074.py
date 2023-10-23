from random import randint
num = ((randint(1, 10)), (randint(1, 10)), (randint(1, 10)),
       (randint(1, 10)), (randint(1, 10)), (randint(1, 10)))
for n in num:
    print(f'| {n}', end=' ')
print(f'|\n\033[1;31mO Menor valor foi {(min(num))}\033[m')
print(f'\033[1;32mO Maior valor foi {max(num)}\033[m')
print('FIM!')
#print('O menor para o maior é {}'.format(sorted(num)))

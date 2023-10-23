elementos = int(input('Quantos termos você quer? '))
t1 = 0
t2 = 1
cont = 3
print('{}--{}'.format(t1, t2), end='')
while cont <= elementos:
    t3 = t1 + t2
    print(f'--{t3}', end='')
    cont += 1
    t1 = t2
    t2 = t3
print('\n')
print('FIM')

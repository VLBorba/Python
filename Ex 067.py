while True:
    n = int(input('Digite um valor: '))
    if n < 0:
        break
    print('-'*20)
    for t in range(1, 11):
        print(f'{n} * {t} = {n*t}')
print('\033[1;31mNEGATIVO NÃOOOO!!!\033[m')

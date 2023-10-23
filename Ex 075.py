tupla = (int(input('Digite o valor 1: ')), int(input('Digite o valor 1: ')),
         int(input('Digite o valor 1: ')), int(input('Digite o valor 1: ')))
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro 3 apareceu na posição {tupla.index(3)+1}')
print('Os valores pares são: ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

número = int(input('Digite um número: '))
total = 0
for c in range(1, número+1):
    if número % c == 0:
        total += 1
        print('\033[1;4;32m')
    else:
        print('\033[1;4;31m')
    print(c, end='')
if total == 2:
    print('\n\033[m\033[1;4mNumero primo!\033[m')
else:
    print('\n\033[1;mNão é primo!\033[m')

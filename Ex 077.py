tupla = ('banana', 'melancia', 'manga', 'kiwi', 'uva', 'morango', 'laranja')
for item in tupla:
    print(f'\nNa palavra \033[4m{item.capitalize()}\033[m as vogais são:  ', end='')
    for letras in item:
        if letras in 'aeiou':
            print(f'\033[4m{letras}\033[m', end=' ')

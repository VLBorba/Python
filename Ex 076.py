print('\033[1;36m-'*50)
print('{: ^50}'.format(' Frigobar & Adega '))
print('-'*50)
tabela = ('Vinho', 21.99,
          'Cerveja', 6.99,
          'Whisky', 59.99,
          'Vodka', 24.99,
          'Licor', 17.99,
          'Gin', 84.99)
for produto in range(0, len(tabela)):
    if produto % 2 == 0:
        print(f'\033[m\033[1;36;40m{tabela[produto]:.<43}\033[m', end='')
    else:
        print(f'\033[1;36;40m$ {tabela[produto]:.>}\033[m')
print('\033[1;36m-'*50)

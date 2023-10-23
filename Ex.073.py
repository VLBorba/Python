cont = 1
print('\033[1;7;40m-{:-^85}\033[m'.format('TABELA'))
print('-'*90)
brasileirão = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fortaleza',
               'Fluminense', 'Athletico-Pr', 'Atético-MG', 'São Paulo', 'Cuiabá', 'Internacional',
               'Corinthians', 'Santos', 'Cruzeiro', 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'América-MG')
print('\033[1;32mO G5 (Os 5 melhores) são {}\033[m'.format(brasileirão[0:5]))
print('-'*90)
print('\033[1;31mO Z4 (Zona de rebaixamento) é {}\033[m)'.format(brasileirão[16:20]))
print('-'*90)
print('\033[1;37mOs times em ordem alfabética é {}\033[m'.format(sorted(brasileirão)))
print('-'*90)
print('\033[1;34mO Corinthians é o {}° Colocado\033[m'.format(brasileirão.index('Corinthians')+1))
print('-'*90)
print('\033[1;33;40mClassificação atual\033[m')
for times in brasileirão:
    print(f'\033[1;33;40m{cont}°{times}\033[m')
    cont += 1

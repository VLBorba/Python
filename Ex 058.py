print('\033[1;33m-'*49)
print('Vou pensar em um valor de 0-10.. Tente adivinhar!')
print('-'*49)
from random import randint
tentativas = 1
pc = randint(0, 10)
jogador = int(input('\033[mDigite um valor de 0-10: '))
while pc != jogador:
    if jogador < pc:
        print('\033[1;34mMais...\033[m')
    else:
        print('\033[1;31mMenos...\033[m')
    jogador = int(input('Tente novamente! Digite mais um valor entre 0-10: '))
    tentativas += 1
print('Acertou! a quantidade de tentativas foi {}! e sua resposta e do computador foram {}'.format(tentativas, pc))

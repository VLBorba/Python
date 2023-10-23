from random import randint
win = 0
while True:
    escolha = int(input('Você é ímpar(1) ou par(2)? '))
    jogador = int(input('Digite um valor: '))
    pc = randint(1, 10)
    s = jogador + pc
    if escolha == 1:
        if s % 2 == 0:
            print(f'\033[1;31mVocê perder o resultado foi {s}\033[m')
            break
        else:
            print(f'\033[1;32mVocê ganhou o resultado foi {s}\033[m')
            win += 1
    if escolha == 2:
        if s % 2 == 0:
            print(f'\033[1;32mVocê ganhou o resultado foi {s}\033[m')
            win += 1
        else:
            print(f'\033[1;31mVocê perdeu o resultado foi {s}\033[m')
            break
    if escolha > 2 or escolha < 1:
        print('\033[1;4;37m[Escohla incorreta]\033[m')
print(f'O Total de vitórias consecultivas foram \033[1;4;35m{win}\033[m')

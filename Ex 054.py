from datetime import date
maior = 0
menor = 0
atual = date.today().year
for ano in range(1, 8):
    idade = int(input('Digite o ano de nascimento da {}ºPessoa: '.format(ano)))
    if atual-idade >= 18:
        maior += 1
    else:
        menor += 1
print('Temos {} pessoas \033[1;4;36mMaiores\033[m de idade.'.format(maior))
print('Temos {} pessoas \033[1;4;35mMenores\033[m de idade.'.format(menor))

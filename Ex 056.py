média = 0
mulheres = 0
velho = 0
nomevelho = ''
for pessoas in range(1, 5):
    print('-'*30)
    nome = input('Digite o nome da {}º: '.format(pessoas)).strip().capitalize()
    sexo = input('Digite o sexo [M/F] da {}º: '.format(pessoas)).lower().strip()
    idade = int(input('Digite a idade da {}º: '.format(pessoas)))
    média += (idade)/4
    if sexo == 'f' and idade < 20:
            mulheres += 1
    if sexo == 'm' and pessoas == 1:
            velho = idade
            nomevelho = nome
    elif sexo == 'm' and idade > velho:
            velho = idade
            nomevelho = nome
    if sexo != 'f' and sexo != 'm':
        print('[SEXO INVÁLIDO]')
print('-'*30)
print(f'O homem mais velho tem \033[1;4m{velho}\033[m anos e se chama \033[1;4m{nomevelho}\033[m')
print(f'Temos \033[1;4m{mulheres}\033[m Mulheres com - de 20 anos')
print(f'Média de idade ({média}) anos')

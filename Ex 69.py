contidade = conthomem = contmulher = cont20anos = 0
print('-*-'*5)
print('|\033[4mCadastro 069\033[m|')
print('-*-'*5)
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo[0] not in 'mf':
        sexo = input('Digite seu sexo [Masc/Fem]: ').lower().split()[0]
    continuar = input('Deseja continuar? ').lower().split()[0]
    if idade > 18:
        contidade += 1
    if sexo[0] == 'm':
        conthomem += 1
    if sexo[0] == 'f' and idade < 20:
        cont20anos += 1
    if continuar[0] == 's':
        print('-'*30)
    else: break
print('-'*30)
print(f'Temos {contidade} pessoas com + de 18 anos.')
print(f'Temos {conthomem} Homens cadastrados.')
print(f'Temos {cont20anos} Mulheres com - de 20 anos.')

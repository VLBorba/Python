valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro: '))
print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programar''')
operação = int(input('Qual a operação? '))
while operação != 5:
    if operação == 1:
        soma = valor1+valor2
        print(f'{valor1} + {valor2} = {soma}')
    elif operação == 2:
        multiplicar = valor1*valor2
        print(f'{valor1} * {valor2} = {multiplicar}')
    elif operação == 3:
        if valor1 > valor2:
            print(f'{valor1} > {valor2}')
        elif valor2 > valor1:
            print(f'{valor2} > {valor1}')
        else:
            print('Os valores são iguais!')
    elif operação == 4:
        valor1 = int(input('Digite o 1° novo valor: '))
        valor2 = int(input('Digite o 2° novo valor: '))
    else:
        print('[FALHA] Comando não reconhecido, Tente novamente!')
    operação = int(input('Qual a operação? '))
print('\033[1;4mFim do programa!\033[m')

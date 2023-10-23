soma = 0
contador = 0
for inteiros in range(1, 7):
    valor = int(input('Digite o {}º valor: '.format(inteiros)))
    if valor % 2 == 0:
        soma = soma + valor
        contador += 1
print('Você digitou {} pares.'.format(contador))
print('A soma dos pares da sua sequência é: \033[1;4m{}\033[m'.format(soma))

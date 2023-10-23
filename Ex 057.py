sexo = input('Digite seu sexo [m/f]: ').lower().strip()[0]
while sexo not in 'mf':
    sexo = input('Sexo inválido, tente novamente: ').lower().strip()[0]
print(f'Sexo "{sexo}" registrado com sucesso.')

saque = int(input('Quanto você quer sacar? $'))
total = saque
nota = 50
cont = 0
while True:
   if total >= nota:
       total -= nota
       cont += 1
   else:
       if nota == 50:
           nota = 20
       elif nota == 20:
           nota = 10
       elif nota == 10:
           nota = 1
       if nota > 0:
           print(f'Total de notas foi {cont} no valo de {nota}')
       if total == 0:
           break
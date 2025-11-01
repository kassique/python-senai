import os
os.system('cls')

idade = int(input('Digite a idade:'))
altura = float(input('Digite a altura:'))

if(idade == 16 and altura >= 1.70):
    print('Aprovada! :D')
else:
    print('Reprovada! D:')
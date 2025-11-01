import os
os.system('cls')

idade = int(input('Digite a idade:'))

if(idade <= 11):
    print('Infantil')
elif(idade >= 12 and idade <= 17):
    print('Adolescente')
elif(idade >= 18 and idade <= 24):
    print('Jovem')
else:
    print('Adulto')
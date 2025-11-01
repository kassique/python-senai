import os
os.system('cls')

idade = int(input('Digite a idade:'))
altura = float(input('Digite a altura:'))
valida_idade = idade == 16
valida_altura = altura >= 1.70

if valida_idade and valida_altura:
    print('Modelo aprovada! :D')
else:
    print('Modelo reprovada! D:')
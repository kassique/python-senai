import os
os.system('cls')

nota1 = float(input('Digite o valor da nota:'))
nota2 = float(input('Digite o valor da nota:'))
nota3 = float(input('Digite o valor da nota:'))
nota4 = float(input('Digite o valor da nota:'))
media = (nota1 + nota2 + nota3 + nota4) / 4

if(media >= 7):
    print('Aprovado! :D')
else:
    print('Reprovado! D:')
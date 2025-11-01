import os
os.system('cls')

termo1 = int(input('Digite o valor do termo:'))
termo2 = int(input('Digite o valor do termo:'))
razao = termo2 / termo1
termo5 = termo1 * (razao ** 4)

print(f'O décimo termo da PA é: {termo5}')
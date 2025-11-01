import os
os.system('cls')

valor = int(input('Digite o valor do produto:'))
desconto = valor / 100 * 9

print(f'O desconto do valor de {valor} reais foi de {desconto} reais')
import os
os.system('cls')

numero01 = float(input('Digite o dividendo:'))
numero02 = float(input('Digite o divisor:'))
total = numero01 / numero02
resto = numero01 % numero02

print(f'O quociente da divisão é: {total}')
print(f'O resto da divisão é: {resto}')
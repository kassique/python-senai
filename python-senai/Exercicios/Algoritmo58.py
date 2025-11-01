import os
os.system('cls')
import math

numero1 = int(input('Digite um valor:'))
numero2 = int(input('Digite um valor:'))
numero3 = int(input('Digite um valor:'))
x = numero1 + (numero2 / (numero3 + numero1)) + 2 * (numero1 - numero2) + math.log(64)

print(f'O valor de x é: {x}')
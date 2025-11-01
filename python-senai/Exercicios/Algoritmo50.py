import os
os.system('cls')
import math

base = int(input('Digite a base do triângulo:'))
altura = int(input('Digite a altura do triângulo:'))
perimetro = (base ** 2) + (altura ** 2)
area = base * altura
diagonal = math.sqrt((base ** 2) + (altura ** 2))

print(f'O perímetro é: {perimetro}')
print(f'A área é: {area}')
print(f'A diagonal é: {diagonal}')
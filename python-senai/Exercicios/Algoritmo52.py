import os
os.system('cls')
import math

lado = int(input('Digite o valor do lado do quadrado:'))
perimetro = 4 * lado
area = lado ** 2
diagonal = lado * math.sqrt(2)

print(f'O perímetro do quadrado é: {perimetro}')
print(f'A área do quadrado é: {area}')
print(f'A diagonal do quadrado é: {diagonal}')
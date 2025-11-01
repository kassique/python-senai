import os
os.system('cls')
import math

angulo = float(input('Digite o valor do ângulo:'))
radiano = math.radians(angulo)
seno = math.sin(radiano)
coseno = math.cos(radiano)
tangente = math.tan(radiano)
secante = 1 / coseno
cotangente = 1 / tangente
cosecante = 1 / seno

print(f'Seno: {seno}')
print(f'Coseno: {coseno}')
print(f'Tangente: {tangente}')
print(f'Secante: {secante}')
print(f'Co-tangente: {cotangente}')
print(f'Co-secante: {cosecante}')
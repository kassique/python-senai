import os
os.system('cls')
import math

a = int(input('Digite o valor do lado a:'))
b = int(input('Digite o valor do lado b:'))
c = int(input('Digite o valor do lado c:'))

diagonal = math.sqrt((a ** 2) + (b ** 2) + (c ** 2))

print(f'A diagonal do paralelepípedo é: {diagonal}')
import os
os.system('cls')
import math

cateto1 = int(input('Digite o valor do cateto:'))
cateto2 = int(input('Digite o valor do cateto:'))
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print(f'O valor da hipotenusa é: {hipotenusa}')
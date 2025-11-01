import os
os.system('cls')
import math

nota1 = float(input('Digite o valor da nota:'))
nota2 = float(input('Digite o valor da nota:'))
media = (nota1 + nota2) / 2
arredondada = round(media)
truncada = math.trunc(media)

print(f'A média entre as notas é: {media}')
print(f'A média arredondada entre as notas é: {arredondada}')
print(f'A média truncada entre as notas é: {truncada}')
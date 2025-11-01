import os
os.system('cls')

quantidade = 5
valor = 2.800
total = quantidade * valor
desconto = quantidade * (valor - ((valor / 100) * 15))

print(total)
print(desconto)
import os
os.system('cls')

saldo = float(input('Digite o saldo atual:'))
reajuste = saldo + ((saldo / 100) * 1)

print(f'O novo saldo, considerando o reajuste de 1% é de: {reajuste}')
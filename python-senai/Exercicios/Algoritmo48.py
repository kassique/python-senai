import os
os.system('cls')

valor_salario = float(input('Digite o valor do salário mínimo:'))
quantidade_quilowatt = int(input('Digite a quantidade de quilowatts gastos:'))

setimo_salario = valor_salario / 7
valor_quilowatt = setimo_salario / 100
valor_pago = valor_quilowatt * quantidade_quilowatt
reajuste = valor_pago - ((valor_pago / 100) * 10)

print(f'O valor de cada quilowatt é: {valor_quilowatt}')
print(f'O valor a ser pago é: {valor_pago}')
print(f'O valor a ser pago, considerando o reajuste é: {reajuste}')
import os
os.system('cls')

valor_hora = float(input('Digite o valor da hora:'))
quantidade_hora = int(input('Digite a quantidade de horas:'))
desconto_inss = int(input('Digite a porcentagem de desconto do INSS:'))
salario_bruto = valor_hora * quantidade_hora
salario_liquido = salario_bruto - ((salario_bruto / 100) * desconto_inss)

print(f'O valor do salário líquido é {salario_liquido} reais')
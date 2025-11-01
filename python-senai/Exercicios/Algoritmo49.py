import os
os.system('cls')

nome = input('Digite um nome:')
primeiro = nome[0]
ultimo = nome[-1]
primeiro_terceiro = nome[0:3]
quarto = nome[3]
exceto_primeiro = nome[1::]
dois_ultimos = nome[-2::]

print(f'O nome é: {nome}')
print(f'O primeiro caractere é: {primeiro}')
print(f'O último caractere é: {ultimo}')
print(f'Do primeiro até o terceiro caractere: {primeiro_terceiro}')
print(f'O quarto caractere é: {quarto}')
print(f'Todos os caracteres, exceto o primeiro: {exceto_primeiro}')
print(f'Os dois últimos caracteres: {dois_ultimos}')
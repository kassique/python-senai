import os
os.system('cls')

"""
Variáveis em Python se adaptam ao tipo de dado inserido. Os tipos são:
str = Textos
int = Números inteiros (1, 2, 3)
float = Números reais (1.1, 2.2, 3.3)
boolean = True ou False
"""

nome = 'Senai'
numero = 25
valor = 3.5
resultado = True

print(type(nome))
print(type(numero))
print(type(valor))
print(type(resultado))

#Todo input é por padrão uma string, a menos que seja convertido

dado = (input('Digite algo:'))
print(type(dado))
dado = str(input('Digite algo:'))
print(type(dado))
dado = int(input('Digite algo:'))
print(type(dado))
dado = float(input('Digite algo:'))
print(type(dado))
dado = bool(input('Digite algo:'))
print(type(dado))
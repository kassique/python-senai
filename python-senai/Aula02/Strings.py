import os
os.system('cls')

nome = 'Anakin'

print(len(nome)) #Conta o total de caracteres dentro da string
print(nome[0]) #Busca o primeiro caractere dentro da string
print(nome[-1]) #Busca o ultimo caractere dentro da string
print(nome[0:3]) #Busca os três primeiros caracteres dentro da string
print(nome[::2]) #Busca de 2 em 2 caracteres dentro da string
print(nome[::-1]) #Inverte os caracteres da string
print(nome.lower()) #Formata o texto para minúsculas
print(nome.upper()) #Formata o texto para maiúsculas

nome = 'Darth Vader'

print(nome.replace('Vader', 'Sidious')) #Substitui uma string
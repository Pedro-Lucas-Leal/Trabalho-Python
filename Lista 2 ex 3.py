import math

numero = float(input('Insira algum número e te mostrarei se ele é inteiro ou decimal: '))

comparacao = numero
numero = math.ceil(numero)

if numero == comparacao:
    print('Seu número é inteiro.')
else:
    print('Seu número é decimal.')

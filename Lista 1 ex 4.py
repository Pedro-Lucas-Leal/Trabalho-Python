from math import ceil

areaPintada = float(input('Digite a área a ser pintada em metros quadrados: '))

litrosTotal = areaPintada / 3
latas = litrosTotal / 18
latas = ceil(latas)
precoTotal = latas * 80

print(f'Você precisará de {latas} latas, totalizando um valor de {precoTotal} reais')
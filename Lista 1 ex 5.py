import math

areaPintada = float(input('Quantos metros quadrados você quer pintar? '))

litrosTotal = areaPintada / 6
latas = litrosTotal / 18
galao = litrosTotal / 3.6
latas = math.ceil(latas)
galao = math.ceil(galao)
misturadoLatas = litrosTotal / 18
misturadoLatas = math.floor(misturadoLatas)
misturadoGaloes = (litrosTotal - (misturadoLatas*18)) / 3.6
misturadoGaloes = math.ceil(misturadoGaloes)
precoTotal = (misturadoLatas*80) + (misturadoGaloes*25)

print(f'Você precisará de {litrosTotal} litros no total, e tem 3 opções de compras...\n\n1- Caso você compre somente latas, você precisará comprar {latas} lata(s), o que totalizará no total de {latas*80} reais.\n\n2- Se preferir, pode comprar apenas galões, resultando em {galao*25} reais na compra de {galao} galões.\n3- Misturando latas e galoes, você preisará comprar {misturadoLatas} latas ({misturadoLatas*80} reais) e {misturadoGaloes} galoes ({misturadoGaloes*25} reais), totalizando {precoTotal} reais!')

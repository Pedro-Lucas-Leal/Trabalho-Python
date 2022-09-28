peso = int(input("Insira o peso dos peixes: "))

if peso <= 50:
    print(f'Como o peso não ultrapassou 50 kg, você não precisará pagar multa.')
else:
    excesso = peso - 50
    multa = 4*excesso
    print(f'Poxa, o seu peso ultrapassou o limite em {excesso} kg. De acordo com a regra, você terá que pagar {multa} reais de multa... ')

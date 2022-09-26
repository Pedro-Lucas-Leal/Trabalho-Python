alturasIdades = []

for x in range(5):
    altura = float(input(f'Insira a altura da {x+1}ª pessoa em metros: '))
    alturasIdades.append(altura)
    idade = int(input(f'Agora coloque a idade da {x+1}ª pessoa: '))
    alturasIdades.append(idade)
alturasIdades.reverse()
print(alturasIdades)

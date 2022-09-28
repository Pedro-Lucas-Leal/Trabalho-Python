listaInteiros = []
x = 1

while x <= 10:
    entradaDados = int(input(f'Digite o {x}º número: '))
    entradaDados = entradaDados * entradaDados
    listaInteiros.append(entradaDados)
    x = x + 1

print(listaInteiros)

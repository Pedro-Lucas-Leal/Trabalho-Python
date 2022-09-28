listaUm = []
listaDois = []
listaTres = []
x = 1

while x <= 10:
    entrada_lista_um = input(f'Digite o {x}º número da primeira lista: ')
    listaUm.append(entrada_lista_um)
    listaTres.append(entrada_lista_um)
    entrada_lista_dois = input(f'Agora insira o {x}º número da segunda lista: ')
    listaDois.append(entrada_lista_dois)
    listaTres.append(entrada_lista_dois)
    x = x + 1

print(listaTres)

import math

saque = int(
    input("Insira a quantidade que deseja sacar (entre 10 e 600 reais): "))

if saque < 10 or saque > 600:
    print('Valor inválido! Insira um valor entre 10 e 600.')
else:
    notasCem = saque / 100
    notasCem = math.floor(notasCem)
    saque = saque - (notasCem*100)
    notasCinquenta = saque / 50
    notasCinquenta = math.floor(notasCinquenta)
    saque = saque - (notasCinquenta * 50)
    notasDez = saque / 10
    notasDez = math.floor(notasDez)
    saque = saque - (notasDez*10)
    notasCinco = saque / 5
    notasCinco = math.floor(notasCinco)
    saque = saque - (notasCinco * 5)
    notasUm = saque / 1
    notasUm = math.floor(notasUm)

    print(f'O valor será dado em:\n\n{notasCem} notas de cem reais.\n{notasCinquenta} notas de cinquenta reais.\n{notasDez} notas de dez reais.\n{notasCinco} notas de cinco reais.\n{notasUm} notas de um real.')

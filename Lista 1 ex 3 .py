salarioHora = float(input('Quantos reais você ganha por hora?\n'))
horasTrabalhadas = float(input('E quantas horas por mês você trabalha?\n'))

salarioBruto = salarioHora*horasTrabalhadas
impostoRenda = salarioBruto*(11/100)
inss = salarioBruto*(8/100)
sindicato = salarioBruto*(5/100)
salarioLiquido = salarioBruto - impostoRenda - inss - sindicato

print(f'O seu salário bruto foi: {salarioBruto:.2f}\nForam descontados 11% ({impostoRenda:.2f} reais) para o Imposto de Renda.\nTambém foi descontado 8% ({inss:.2f} reais) para o inss e 5% ({sindicato:.2f} reais) para o sindicato.\nCom todos os descontos aplicados, o seu salário líquido foi {salarioLiquido:.2f}')

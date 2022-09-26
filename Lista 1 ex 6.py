import math
tamanhoArquivo = float(input('Insira o tamanho do arquivo em MB: '))
velocidadeInternet = float(input('Agora digite a velocidade em Mbps '))

tempo = ((velocidadeInternet/8)*60) / tamanhoArquivo
tempo = math.ceil(tempo)
print(f'O seu download levará aproximadamente {tempo:.0f} minutos para ser concluído')
1
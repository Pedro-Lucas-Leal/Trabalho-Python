sexo = input('Vamos calcular o seu peso ideal!\nPrimeiramente, você é homem ou mulher?\n\nh - HOMEM\nm - MULHER\n\n')
altura = float(input('\nAgora insira a sua altura em metros: '))

match sexo:
    case 'h':
        peso = (72.7*altura) - 58
        print(f'Seu peso ideal é {peso:.3f} kg')
    case 'm':
        peso = (61.1*altura) - 44.7
        print(f'Seu peso ideal é {peso:.3f} kg')
    case other:
        print('Utilize apenas h ou m para selecionar o seu sexo')

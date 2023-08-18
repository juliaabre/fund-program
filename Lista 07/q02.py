def Notas(nota):
    if 0 <= nota <=4.9:
        conceito = 'D'
    elif 5 <= nota <= 6.9:
        conceito = 'C'
    elif 7 <= nota <= 8.9:
        conceito = 'B'
    elif 9 <= nota <= 10:
        conceito = 'A'
    else:
        print('Nota Inválida')
    return conceito

nota = float(input('Informe a média final: '))
print(f'O conceito da nota informada é {Notas(nota)}')

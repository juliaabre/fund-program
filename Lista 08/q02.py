def SomaDiagonal(matriz):
    sum = 0
    for i in range(3):
        for p in range(3):
            print(f'{matriz[i][p]:^5}', end="")
        print("")

    for i in range(0, 3):
        print(matriz[i][i])
        sum += (matriz[i][i])
    print(f'A soma da diagonal principal é: {sum}')
        


matriz = [[9, 4, 7], [5, 1, 8], [0, 3, 9]]
SomaDiagonal(matriz)
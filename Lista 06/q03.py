from random import randint

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = randint(0, 10)

def QuadradoMagico():
    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz[1][1] + matriz[2][2] == matriz[0][2] + matriz[1][1] + matriz[2][0]:
        return print('A matriz é um quadrado mágico.')
    else:
        return print('NÃO é um quadrado mágico.')
    

for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end='')
    print()
QuadradoMagico()

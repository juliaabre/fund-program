matriz = [[], [], []]

def Soma_Linha(matriz):
    soma1 = soma2 = soma3 = menor = 0
    for l in range(3):
        soma1 += matriz[0][l]
    for l in range(3):
        soma2 += matriz[1][l]
    for l in range(3):
        soma3 += matriz[2][l]
    for i in range(3):
        if i == 0:
            menor = soma1
        elif soma2 < menor:
            menor = soma2
        elif soma3 < menor:
            menor = soma3
    resp = print(f'A soma da menor linha é: {menor}')
    return resp

def Soma_Coluna(matriz):
    soma1 = soma2 = soma3 = maior = 0
    for c in range(3):
        soma1 += matriz[c][0]
    for c in range(3):
        soma2 += matriz[c][1]
    for c in range(3):
        soma3 += matriz[c][2]
    for i in range(3):
        if i == 0:
            maior = soma1
        elif soma2 > maior:
            maior = soma2
        elif soma3 > maior:
            maior = soma3
    resp = print(f'A soma da maior coluna é: {maior}')
    return resp
    
    
for i in range(0, 3):
    for r in range(0, 3):
        n = int(input(f'Digite um número para [{i}, {r}]: '))
        matriz[i].append(n)

for l in range(3):
    for c in range(3):
        print(f'{matriz[l][c]:^5}', end='')
    print()

linha = Soma_Linha(matriz)
coluna = Soma_Coluna(matriz)

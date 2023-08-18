from random import randint

def GeraMatriz(dimensao):
    matriz = []
    for i in range(0, dimensao):
        matriz.append([randint(0,100), randint(1,100), randint(0,100)])
    return matriz

def Vetor(matriz):
    vetor = []
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            vetor.append(matriz[i][j])
    return vetor

def MaiorValor(vetor, tamanho, i):
    if tamanho == 0:
        return vetor[i]
    else:
        if vetor[tamanho-1] > vetor[i]:
            return MaiorValor(vetor, tamanho-1, tamanho-1)
        else:
            return MaiorValor(vetor, tamanho-1, i)
    

matriz = GeraMatriz(3)
print(matriz)

vetor = Vetor(matriz)
tvetor = len(vetor)
print(MaiorValor(vetor, tvetor, 0))


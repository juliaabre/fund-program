from random import randint

vetor = []
repetidos = 0

for v in range(0, 10):
    n = randint(0, 100)
    if n in vetor:
        vetor.append(n)
        repetidos +=1
    else:
        vetor.append(n)

print(f'A lista gerada é {vetor}')
print(f'A quantidade de números repetidos é {repetidos}')
